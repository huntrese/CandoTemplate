import pygame
import os
import sys
from pygame.locals import *
from tkinter import filedialog, Tk
import tkinter as tk
from PIL import Image
import math
import shutil
from tkinter.colorchooser import askcolor


class PygameFileUploader:
    def __init__(self,replacememnts):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.BG_COLOR = (255, 255, 255)
        self.TEXT_COLOR = (0, 0, 0)
        self.IMAGE_SIZE = (100, 100)
        self.UPLOADED = [False]
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pygame File Uploader")
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.image_paths = []
        self.image_surfaces = []
        self.image_rects = []
        self.image_order = []
        self.running = True
        self.dragging = False
        self.dragged_image_index = -1
        self.submitted = 0

        self.IMAGE_AREA_X = 50
        self.IMAGE_AREA_Y = 50
        self.IMAGE_AREA_WIDTH = 700
        self.IMAGE_AREA_HEIGHT = 400

        self.backgroundColor = [(17, 24, 34)]
        self.titleColor = [(109, 109, 109)]
        self.replacements=replacememnts

    def load_and_resize_image(self, image_path):
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, self.IMAGE_SIZE)
            return image
        except pygame.error:
            return None

    def update_index(self):
        with open("test_py\\index_template.php", "r", encoding="utf-8") as f:
            data = f.read()
            for key, value in self.replacements.items():
                if key == "bg_color":
                    value = self.convert(self.backgroundColor[0])
                data = data.replace("{" + key + "}", str(value))
            with open("src\\public\\index.php", "w", encoding="utf-8") as file:
                file.write(data)
            print(data)
        with open("test_py\\style copy.css", "r+", encoding="utf-8") as file:
            styles = file.read()
            styles = styles.replace("#259DD7", str(self.titleColor[0]))
            with open("src\\public\\css\\style.css", "w", encoding="utf-8") as f:
                f.write(styles)

    def open_file_dialog(self):
        root = Tk()
        root.withdraw()
        self.UPLOADED[0] = True
        file_paths = filedialog.askopenfilenames(title="Open Images", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.webp")])
        root.destroy()

        converted_file_paths = []
        for file_path in file_paths:
            if file_path.lower().endswith(".webp"):
                try:
                    with Image.open(file_path) as img:
                        jpg_path = file_path[:-5] + ".jpg"
                        img.convert("RGB").save(jpg_path, "JPEG")
                    converted_file_paths.append(jpg_path)
                except Exception as e:
                    print(f"Failed to convert {file_path} to jpg: {e}")
            else:
                converted_file_paths.append(file_path)

        return converted_file_paths

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.TEXT_COLOR)
        self.screen.blit(text_surface, (x, y))

    def reorder_images(self):
        for i, order in enumerate(self.image_order):
            x = self.IMAGE_AREA_X + i * (self.IMAGE_SIZE[0] + 20)
            y = self.IMAGE_AREA_Y
            self.image_rects[order] = pygame.Rect(x, y, self.IMAGE_SIZE[0], self.IMAGE_SIZE[1])

    def open_color_picker(self, which):
        root = tk.Tk()
        root.withdraw()
        color = askcolor()[1]
        root.destroy()
        match(which):
            case 0:
                self.backgroundColor[0] = color
            case 1:
                self.titleColor[0] = color
            case _:
                print("color error")

    def convert(self, value):
        if type(value) == str:
            return value
        elif type(value) == int:
            return f"#{hex(value)[2:]}"
        else:
            return f"#{hex(value)[2:]}"

    def run(self):
        while self.running:
            self.screen.fill(self.BG_COLOR)
            names = ["b1-3.jpg", "01.jpg", "02.jpg", "03.jpg", "04.jpg"]
            x = 50
            for image_path, rect in zip(self.image_paths, self.image_rects):
                image_surface = self.load_and_resize_image(image_path)
                if image_surface:
                    self.screen.blit(image_surface, rect.topleft)
                    self.draw_text(os.path.basename(names[self.image_rects.index(rect)]), x, rect.bottom)
                    x += 120

            if not self.UPLOADED[0]:
                pygame.draw.rect(self.screen, (0, 128, 255), (50, 500, 200, 50))
                self.draw_text("Upload Images (Press 'O')", 55, 510)
            else:
                submit = pygame.draw.rect(self.screen, (144, 144, 144), (50, 200, 200, 50))
                self.draw_text("Submit", 55, 205)
                bg_color = pygame.draw.rect(self.screen, self.backgroundColor[0], (170, 270, 30, 30))
                self.draw_text("bg color= ", 55, 270)
                title_color = pygame.draw.rect(self.screen, self.titleColor[0], (200, 300, 30, 30))
                self.draw_text("titles color= ", 55, 300)

                # Add the "Save" button
                save_button = pygame.draw.rect(self.screen, (144, 144, 144), (300, 200, 200, 50))
                self.draw_text("Save", 310, 205)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        try:
                        # Check if a click is inside an image
                            for i, rect in enumerate(self.image_rects):
                                if rect.collidepoint(event.pos):
                                    self.dragging = True
                                    self.dragged_image_index = i
                            
                                if self.dragging == False:
                                    if submit.collidepoint(event.pos):
                                        print("Submit button clicked")
                                        self.update_index()
                                        for i, j in enumerate(self.image_order):
                                            shutil.copyfile(self.image_paths[j], f'src\\public\\images\\{names[i]}')
                                    if save_button.collidepoint(event.pos):
                                        print("Save button clicked")

                                            # Copy the new file to the destination directory
                                        shutil.copytree("src\\public\\", f"outputs\\{self.replacements['plasturecap']}")
                        except:
                            pass
                        if bg_color.collidepoint(event.pos):
                            self.open_color_picker(0)
                        elif title_color.collidepoint(event.pos):
                            self.open_color_picker(1)

                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        # Update the position of the dragged image
                        self.image_rects[self.dragged_image_index].move_ip(event.rel)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and self.dragging:
                        self.dragging = False
                        coords = pygame.mouse.get_pos()
                        print("Mouse position:", coords)

                        # Calculate the center of the dragged image
                        dragged_image_center = self.image_rects[self.dragged_image_index].center
                        distances = [math.hypot(image_rect.centerx - dragged_image_center[0], image_rect.centery - dragged_image_center[1]) for image_rect in self.image_rects]
                        dist_new = []
                        for i, j in enumerate(distances):
                            dist_new.append(tuple((j, i)))
                        dist_new = sorted(dist_new)
                        print(dist_new)
                        if dist_new[1][0] != 120.0:
                            self.image_order.clear()
                            self.image_order.append(self.dragged_image_index)

                            dragged_x = self.image_rects[self.dragged_image_index].centerx
                            centerx_rect_tuples = [(rect.centerx, index) for index, rect in enumerate(self.image_rects)]
                            sorted_centerx_rect_tuples = sorted(centerx_rect_tuples, key=lambda x: x[0])
                            for rect in sorted_centerx_rect_tuples:
                                if rect[0] < dragged_x:
                                    insert_index = self.image_order.index(self.dragged_image_index)
                                    self.image_order.insert(insert_index, rect[1])
                                elif rect[0] > dragged_x:
                                    self.image_order.append(rect[1])

                            print("New Image Order:", self.image_order)
                            self.reorder_images()

                elif event.type == KEYDOWN:
                    if event.key == K_o:
                        new_image_paths = self.open_file_dialog()
                        for new_path in new_image_paths:
                            if new_path not in self.image_paths:
                                self.image_paths.append(new_path)
                                self.image_surfaces.append(self.load_and_resize_image(new_path))
                                self.image_rects.append(pygame.Rect(0, 0, self.IMAGE_SIZE[0], self.IMAGE_SIZE[1]))
                        self.image_order.clear()
                        for i in range(len(self.image_rects)):
                            self.image_order.append(i)
                        self.reorder_images()

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    uploader = PygameFileUploader()
    uploader.run()

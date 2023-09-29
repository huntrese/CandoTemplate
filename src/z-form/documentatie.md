index.php
Prinum rand de cod trebuie sa fie <? include_once('s-config.php'); ?>

apoti in in formular intre tagurile <form> si </form> se va pune codul
<? echo formImputs(); ?>
in action="send-form.php"

gaseti in cod javascriptul de genul acesta si il cometati cu codurile  <!-- -->
dupa cum e indicat mai jos
<!--
<script src='https://cpa78.info/track-.js' hash='2014ef995b8986381dc6378ff14a6f77' id='wildo'></script>
<script src='https://cpa78.info/widgets-.js' hash='2014ef995b8986381dc6378ff14a6f77' id='wildoWidgets'></script>
-->

In mapa cu proiectul trebuie de pus fisierul send-form.php din mapa pentru-site

1. creezi bot telegram, poti face asta doar oadata si sa folosesti pentru toate landingurile acelasi bot - (vezi in video)
2. ii inchizi private mode "Privacy mode is disabled for [denumirea botului]" (vezi in video)
    Bot Settings > Group Privacy > turn off
3. pui token-ul in s-config.php
4. creezi grup cu botul pentru leaduri fake, poti face pentru fiecare landing aparte sau poti avea unu comun (vezi in video)
5. scrii cate un mesaj in giecare grup.
6. intri pe linkul site/s-config.php?telegram=1 de exemplu  http://rimishop.ru/cam3/s-config.php?telegram=1
si gasesti
[chat] => Array
   (
       [id] => -525055204
       [title] => Leaduri Fake
       [type] => group
       [all_members_are_administrators] => 1
   )
   ei id-ul "-525055204" si il pui in s-config
   pui id-ul in s-config.php
(Vezi in video)
7. creezi grup in telegram pentru leduri bune, poti face pentru fiecare landing aparte sau poti avea unu comun (vezi in video)
si repeti scenariu ca si la punctul 6 (vezi in video)
8. in index.php faci configurarile pentru google tabel (vezi in video)
9. poti testa

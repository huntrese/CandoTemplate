<?php
	include_once('../config.php');
	include_once('../form/TelegramBotClass.php');
	include_once('../form/GoogleFormClass.php');

	$Telegram = new TelegramBot($config['telegram']['token'], $config['telegram']['chatID']);
	$Telegram -> setFields($config['telegram']['fields']);
	$TelegramResult = $Telegram -> sendLead($_POST);

	$GoogleForm = new GoogleForm($config['google']['form']);
	$GoogleForm -> setFields($config['google']['fields']);
	$GoogleFormResult = $GoogleForm -> sendLead($_POST);
	
?>

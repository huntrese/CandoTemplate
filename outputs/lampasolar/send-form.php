<?include_once('s-config.php');
$isFakeLead = false;

if(strlen(@$_POST['form-code']) == 0 || codeDecriptor(@$_POST['form-code']) == false){
			$isFakeLead = true;
}

if($isFakeLead == true)
{
		$result = sendFakeLead($config);
		header('location:thanks.html');
} else {
		$result = sendLead($config);
		header('location:thanks.html');
}

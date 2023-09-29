<?
function formImputs(){
  $encriptedCode = codeEncriptor();
  return '<input type="hidden" name="referal" value="' . $_SERVER['HTTP_REFERER'] . '" />
  <input type="hidden" name="ip" value="' . $_SERVER['REMOTE_ADDR'] . '" />
  <input type="hidden" name="utm_source" value="' . $_GET['utm_source'] . '" />
  <input type="hidden" name="utm_medium" value="' . $_GET['utm_medium'] . '" />
  <input type="hidden" name="utm_campaign" value="' . $_GET['utm_campaign'] . '" />
  <input type="hidden" name="utm_term" value="' . $_GET['utm_term'] . '" />
  <input type="hidden" name="utm_content" value="' . $_GET['utm_content'] . '" />
  <input type="hidden" name="fbclid" value="' . $_GET['fbclid'] . '" />
  <input type="hidden" name="form-code" value="' . $encriptedCode . '" />';
}
function codeEncriptor(){

  $date = date('y-m-d');
  $time = time();
  $user = rand(0,1000);
  $code = md5($date.$time.$date.'-'.$user."code");

  $encriptedCode = base64_encode(json_encode([
  	'date'=>$date,
  	'time'=> $time,
  	'user'=> $user,
  	'code'=> $code,
  	'hash'=> md5($_SERVER['REMOTE_ADDR'])
  ]));
  return $encriptedCode;
}
function codeDecriptor($code){
  $code = base64_decode($code);
  $arr = json_decode($code,1);

  $date = date('y-m-d');
  $time = time();
  $user = rand(0,1000);
  $codeMD5 = md5($arr['date'].$arr['time'].$arr['date'].'-'.$arr['user']."code");
  if($codeMD5 == $arr['code'] && $arr['hash'] == md5($_SERVER['REMOTE_ADDR']))
    return true;
  return false;
}
function sendLead($config){
  if(
    strlen(@$config['telegram']['token']) > 0 &&
    strlen(@$config['telegram']['chatID']) > 0 &&
    is_array(@$config['telegram']['fields'])
  ){
    $Telegram = new TelegramBot($config['telegram']['token'], $config['telegram']['chatID']);
  	$Telegram -> setFields($config['telegram']['fields']);
  	$TelegramResult = $Telegram -> sendLead($_POST);
  }
  if(
    strlen(@$config['google']['form']) > 0 &&
    is_array(@$config['google']['fields'])
  ){
  	$GoogleForm = new GoogleForm($config['google']['form']);
  	$GoogleForm -> setFields($config['google']['fields']);
  	$GoogleFormResult = $GoogleForm -> sendLead($_POST);
  }
}
function sendFakeLead($config){
  if(
    strlen(@$config['telegram']['token']) > 0 &&
    strlen(@$config['telegram']['fake-leads']) > 0 &&
    is_array(@$config['telegram']['fields']))
  {
    $Telegram = new TelegramBot($config['telegram']['token'], $config['telegram']['fake-leads']);
  	$Telegram -> setFields($config['telegram']['fields']);
  	$TelegramResult = $Telegram -> sendLead($_POST);
  }
}
function getUpdates($config){
  if(
    strlen(@$config['telegram']['token']) > 0 &&
    is_array(@$config['telegram']['fields']))
  {
    $Telegram = new TelegramBot($config['telegram']['token'],0);
    echo "<pre>";
    print_r($Telegram -> getUpdates());

  }
}
?>

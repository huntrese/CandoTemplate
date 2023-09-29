<?
class TelegramBot {
	var $chatID;
	var $telegramBotToken;
    var $fields = false;
    var $debug = false;
	function __construct($telegramBotToken, $chatID){
		$this -> telegramBotToken = $telegramBotToken;
		$this -> chatID = $chatID;
	}
	function msg($msg) {
	  global $telegrambot,$telegramchatid;
	  $url = 'https://api.telegram.org/bot'.$this -> telegramBotToken.'/sendMessage';
		$data = [
			'chat_id'=> $this -> chatID,
			'text'=> $msg
		];
    $result = file_get_contents($url . "?" . http_build_query($data) );

        if($this -> debug == true)
            echo $result;
	  // $result=file_get_contents($url,false,$context);
	  return $result;
	}
	function getUpdates(){
		$url = 'https://api.telegram.org/bot'.$this -> telegramBotToken.'/getUpdates';
		$result = file_get_contents($url . "?" . http_build_query([]) );
		return json_decode($result, 1);
	}
  function setFields($fields){
    $this -> fields = $fields;
  }

  function sendLead($POST)
  {
    if($this -> fields == false){
      $this -> msg(__LINE__ .": ". __FILE__. " - no fields");
      return false;
    }
    foreach ($this -> fields as $key => $field)
    {
    	if(!empty($POST[$key]))
      {
    		$TelegramMsg .= $field['title'] . ': '. $_POST[$key]."\n";
    	}
    }
    if(!empty($TelegramMsg)){
    	$this -> msg("🎯\n".$TelegramMsg);
      return true;
    }
    return false;
  }
}
?>

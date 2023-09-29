<?
/**
 *
 */
class GoogleForm
{
  var $fields = false;
  var $googleFormURL;
  function __construct($googleFormURL)
  {
    $this -> googleFormURL = $googleFormURL;

  }

  function setFields($fields){
    $this -> fields = $fields;
  }

  function sendLead($POST)
  {
    $post = [];
    foreach ($this -> fields as $key => $field) {

    	if(empty($field['field']))
    		continue;

    	if(!empty($POST[$key])){
    		$post[$field['field']] = $_POST[$key];
    	}
    }
    if(count($post) == 0)
      return false;
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $this -> googleFormURL);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($post));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $server_output = curl_exec($ch);
    curl_close ($ch);
      return true;
  }
}


?>

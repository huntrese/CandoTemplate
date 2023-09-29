<? session_start();
$dir = '../../z-form/';
include_once($dir . 'includes.php');

$config['telegram']= [
  'token' => "1697741125:AAF9dSFwfJdL8iymX5JG7wYzmTMO4mTFPoA",
  'chatID' => '-1001377266957',
  'fake-leads' => '-1001443751998',
  'fields' => [
    'name' => ['title' => 'Nume'],
    'phone' => ['title' => 'Telefon'],
    'city' => ['title' => 'Oras'],
    'street' => ['title' => 'Strada'],
    'product' => ['title' => 'Product'],
    'price' => ['title' => 'Pret'],
    'ip' => ['title' => 'IP'],
    'referal' => ['title' => 'referal'],
    'utm_source' => ['title' => 'utm_source'],
    'utm_medium' => ['title' => 'utm_medium'],
    'utm_campaign' => ['title' => 'utm_campaign'],
    'utm_term' => ['title' => 'utm_term'],
    'utm_content' => ['title' => 'utm_content']

    // 'email' => ['title' => 'Email'],
  ]
];

$config['google'] = [
	  'form' => 'https://docs.google.com/forms/d/e/1FAIpQLScA0j1HAkilSUN5b0q6kjm4bbjKdUKrLjRzEpkAJMNTemSbsw/formResponse',
	  'fields' => [
	  	'name' 				=> ['field' => 'entry.1428500458'],
	  	'phone' 			=> ['field' => 'entry.2129517054'],
	  	'city' 			=> ['field' => 'entry.1208192266'],
	  	'street' 			=> ['field' => 'entry.1075041928'],
	  	'product' 		=> ['field' => 'entry.504087396'],
	  	'price' 		=> ['field' => 'entry.1758073961'],
	  	'ip' 					=> ['field' => 'entry.390382125'],
	  ],
	];


  if($_GET['telegram'] == '1'){
    getUpdates($config);
  }

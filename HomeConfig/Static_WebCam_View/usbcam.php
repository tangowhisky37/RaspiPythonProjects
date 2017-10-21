
<?php

 //Pre-requisities

 // 1> Add the following lines to /etc/sudoers
 // www-data ALL=NOPASSWD: /usr/bin/fswebcam
 // www-data ALL=NOPASSWD: /bin/webcam.sh
 // www-data ALL=NOPASSWD: /bin/chown

 // 2> Create a script called /bin/webcam.sh with the following content
 // sudo /usr/bin/fswebcam -r 640x480 /var/www/html/usbcam/capturedimage.jpg


 //Capturing the image
 //exec('sudo /usr/bin/fswebcam -r 640x480 /var/www/html/usbcam/capturedimage.jpg');
 exec('sudo /bin/webcam.sh');

 //Sleep for 5s
 sleep(5);

 exec('sudo /bin/chown -R www-data:www-data /var/www/html/usbcam/capturedimage.jpg');

 //header("Content-Type: application/html");
 header("Expires: 0");
 //header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
 header("Cache-Control: no-store, no-cache, must-revalidate max-ago=0");
 header("Cache-Control: post-check=0, pre-check=0", false);
 header("Pragma: no-cache");
 
 print "<html>";
 print "<head>";
 print "<title>Webcam View - tangowhisky37 Study</title>";
 //print "<meta http-equiv=refresh content=5";
 print "</head>";
 print "<body>";
 print "<br>";
 print "<br>";
 print "<p align=center>";
 print "<h3 align=center>Webcam View - tangowhisky37 Study</h3>";
 print "</p>";
 print "<br>";
 print "<p align=center>";
 print "<img src=capturedimage.jpg />";
 print "</p>";
 print "<br>";
 print "<p align=center>";
 print "<h3>This page is manually refreshed. Please wait for the entire page to load before you hit refresh.</h3>";
 print "</p>";
 print "</body>";
 print "</html>";

 //Sleep for 10s
 //sleep(10);


?>


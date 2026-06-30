<?php
  phpinfo();
  $directory = "../images/"; // Replace this with the path to your image directory

  // Get all files in the directory
  $files = array_diff(scandir($directory), array('..', '.'));

?>
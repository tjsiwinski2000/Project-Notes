<?php
    $dirPath='./images';
    if ($handle = opendir($dirPath)) {

        while (false !== ($entry = readdir($handle))) {
    
            if ($entry != "." && $entry != "..") {
    
                //echo "$entry\n";
                $filePath=$dirPath . '/'. $entry;
                //echo "$filePath\n";
                echo "<img src='$filePath' alt='$entry' style='max-width: 300px; max-height: 300px;'><br>";
            }
        }
    
        closedir($handle);
    }

 


?>
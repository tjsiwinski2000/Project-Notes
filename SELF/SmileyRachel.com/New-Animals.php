<?php
    echo '<div class="image-row">'; // Start the outer container for the row
   

    $dirPath='./images';
    if ($handle = opendir($dirPath)) {
        $count = 0;

        while (false !== ($entry = readdir($handle))) {
    
            if ($entry != "." && $entry != "..") {


                //echo "$entry\n";
                $filePath=$dirPath . '/'. $entry;
                //echo "$filePath\n";
              
                // Display the image within the current row
                echo '<div class="image-cell" style="width:33%; padding:10px; box-sizing:border-box;">';
                echo "<img src='$filePath' alt='$entry' style='max-width: 400px; max-height: 400px;'><br>";
                echo '</div>';
                echo $count;
                // Open a new row every 3 images
                if ($count % 3 == 0 && $count > 0) {
                    echo '</div>'; // Close the previous row
                    echo '<div class="image-row">'; // Start a new row
                    echo $count;
                }
                $count++;
            }
        }
    
        closedir($handle);
    }

 


?>
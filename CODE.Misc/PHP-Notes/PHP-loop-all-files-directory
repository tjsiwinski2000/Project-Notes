<?php
    echo ' <table style="width:100%">'; // Start the outer container for the row
    echo '<tr>';

    $dirPath='./images';
    if ($handle = opendir($dirPath)) {
        $count = 1;

        while (false !== ($entry = readdir($handle))) {
    
            if ($entry != "." && $entry != "..") {


                //echo "$entry\n";
                $filePath=$dirPath . '/'. $entry;
                //echo "$filePath\n";
              
                // Display the image within the current row
                echo '<td><div class="image-cell" style="width:20%; padding:0px; box-sizing:border-box;">';
                echo "<img src='$filePath' alt='$entry' style='max-width: 350px; max-height: 350px;'>";
                echo $count;
                echo '</div></td>';
                
                // Open a new row every x images
                if ($count % 5 == 0 && $count > 0) {
                    echo '</tr>'; // Close the previous row
                    echo '<tr>'; // Start a new row
                    //echo $count;
                }
                $count++;
            }
        }
    
        closedir($handle);
    }
?>
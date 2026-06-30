<#
AUTHOR  TJ
PURPOSE view CSV as HTML table

DATE 12-02-2024
#>

$file_path= "C:\users\tj\Downloads\status_reports_Mon Dec 02 2024 11_46_55 GMT-0600 (Central Standard Time).csv"
$file_contents= get-content $file_path

$out_file=$PSScriptRoot+"\"+$myInvocation.MyCommand.Name +".html"
Set-Content -Path $out_file -Value "" 
Write-Host "--------"
Write-Host $out_file 
Write-Host "--------"

#Write-Host $file_contents

$final_report=""

foreach ($line in $file_contents)
{
    #Write-Host $line
    #Write-Host "==========================="

    $NewLine=""
    foreach ($element in $line.Split(","))
    {
        $NewLine += "<td>$element</td>"
     }
     #Write-Host $NewLine
     #Write-Host "==========================="
     $final_report+="<tr>$NewLine</tr>"
}

$final_report ="<table border='1'>$final_report</table>"

Add-Content -Path $out_file -Value $final_report
Start-Process  $out_file
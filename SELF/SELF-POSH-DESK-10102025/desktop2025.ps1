# 1010-2025  
# Just fun small app to keep me organized , thanks Gemini
# Get the full path to the text file
$filePath = $PSScriptRoot +"\desktop2025.txt"
Write-Host $filePath

# Read all lines from the file
$lines = Get-Content -Path $filePath
# File length determines legitimate choices for Copy Paste Menu
$max=$lines.Count-1

$count=0

# Check if the file exists
if (-not (Test-Path -Path $filePath -PathType Leaf)) {
    Write-Error "File not found: $filePath"
    return
}
function showCalendar($count)
{
    # Clear the console for a clean menu
    Clear-Host
    Get-Calendar
    $temp=Invoke-RestMethod "http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=78247&aqi=no"
    $temp2=Invoke-RestMethod "http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=92101&aqi=no"
    $temp3=Invoke-RestMethod "http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=11235&aqi=no"
    Write-Host "SanAntonio:$($temp.current.temp_f)||SanDiego:$($temp2.current.temp_f)||Brooklyn:$($temp3.current.temp_f)"
    # Display the menu
    #Write-Host "`n--- Select a line to copy ---" -ForegroundColor Green
    #Write-Host "(Type 'q' or 'quit' to exit or 'r' to refresh) [$count]" -ForegroundColor Green
    #$lines = Get-Content -Path $filePath
    #Write-Host $lines 

}//showCalendar

function CopyPaste($max_lines)
{
 
    for ($i = 0; $i -lt $lines.Count; $i++) 
    {
        Write-Host "[$($i)] $($lines[$i])"
    }

    Write-Host "`n-----------------------------" -ForegroundColor Green

    # Get user input
    $selection = Read-Host "Enter the number of the line you want to copy"
    $selection = [int]$selection
    
    #Write-Host "selection = $selection ; max_lines = $max_lines"
    
    # Validate input
    if ($selection -le $max_lines)
    {
        Write-Host $selection "was inputted"
        $sTemp= $lines[$selection]
        Write-Host $sTemp "will be sent to clipboard"
        Set-Clipboard $null
        $sTemp | Set-Clipboard

        Start-Sleep -Seconds 1
        return $true
    }
    else 
    {
        Write-Host "bad choice bro"
        Start-Sleep -Seconds 2
        return $false
    }
}

# Read all lines from the file
$lines = Get-Content -Path $filePath

do {
    showCalendar($count)
  
     Write-Host  "What do you want to do r)eload c)opy paste menu" -ForegroundColor Green
     $selection = Read-Host

    if ($selection -match "r")
    {
         $some_dots = ".........."
        write-host "Reloading, please standby ..."
        for ($count =10; $count -ne 0; $count--)
        {
                    start-sleep -Milliseconds 300
                    write-host $some_dots.Substring(0,$count)
        }

        showCalendar
    }

    if ($selection -match "c")
    {
        #Stay in copy paste until user input invalid 
        $continue_copy_paste = $true
        do {
            $continue_copy_paste = CopyPaste($max)
        } while ($continue_copy_paste)
    }

} while ($true)

Write-Host "`nExiting menu. Goodbye!" -ForegroundColor Gray
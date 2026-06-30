# 0903-2025  
# Just fun small app to keep me organized , thanks Gemini
# Get the full path to the text file
#$filePath = Read-Host "Enter the full path to the text file"
$filePath = "C:\Users\TJ\source\repos\Project-Notes\SELF\SELF-POSH-DESK\desktop2025.txt"

# Check if the file exists
if (-not (Test-Path -Path $filePath -PathType Leaf)) {
    Write-Error "File not found: $filePath"
    return
}
function showCalendar()
{
    # Clear the console for a clean menu
    Clear-Host
    Get-Calendar
    $temp=Invoke-RestMethod "http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=78247&aqi=no"
    $temp2=Invoke-RestMethod "http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=92101&aqi=no"
    $temp3=Invoke-RestMethod "http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=11235&aqi=no"
    Write-Host "SanAntonio:$($temp.current.temp_f)||SanDiego:$($temp2.current.temp_f)||Brooklyn:$($temp3.current.temp_f)"
    # Display the menu
    Write-Host "`n--- Select a line to copy ---" -ForegroundColor Green
    Write-Host "(Type 'q' or 'quit' to exit or 'r' to refresh)" -ForegroundColor Yellow

}//showCalendar

# Read all lines from the file
$lines = Get-Content -Path $filePath

do {
    showCalendar
    for ($i = 0; $i -lt $lines.Count; $i++) {
        Write-Host "[$($i + 1)] $($lines[$i])"
    }
    Write-Host "`n-----------------------------" -ForegroundColor Green

    # Get user input
    $selection = Read-Host "Enter the number of the line you want to copy"
    
    # Check for exit command
    if ($selection -match '^(q|quit)$') {
        break
    }

    if ($selection -match "r")
    {
        write-host "Reloading, please standby ..."
        start-sleep -Seconds 2
        showCalendar
    }

    # Validate input
    if (($selection -match '^\d+$' -and $selection -ge 1 -and $selection -le $lines.Count)){
        $index = [int]$selection - 1
        $line = $lines[$index]

        # Copy the selected line to the clipboard
        $line | Set-Clipboard

        Write-Host "`nSuccessfully copied: '$line' to the clipboard." -ForegroundColor Cyan
        Start-Sleep -Seconds 2 # Pause for 2 seconds to show confirmation message
    }
    else
    {
        if ($selection -notmatch 'r')
        {
            Write-Host "`nInvalid selection. Please enter a number corresponding to the menu or 'q' to exit." -ForegroundColor Red
            Start-Sleep -Seconds 2 # Pause for 2 seconds to show error message
        }
    }

} while ($true)

Write-Host "`nExiting menu. Goodbye!" -ForegroundColor Gray
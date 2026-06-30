#temp practice for new desktop script

$filePath = $PSScriptRoot +"\desktop2025.txt"
Write-Host $filePath

# Read all lines from the file
$lines = Get-Content -Path $filePath
$max=$lines.Count-1
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
    }
    else 
    {
        Write-Host "bad choice bro"
    }
}
 
do {

    CopyPaste($max)

} while ($true)
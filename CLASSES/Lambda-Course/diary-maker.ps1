#0630-2025 quick diary maker 

#Determine current path
$MyDir = [System.IO.Path]::GetDirectoryName($myInvocation.MyCommand.Definition)

$s = Get-ChildItem *.txt -path $MyDir |Select-Object -First 1
$s = $s -replace "\d"
$s=$s.Replace(".txt","").replace("-","")

$today=[string](Get-Date -Format "MMdd-yyyy")

$fileName=$s+"-"+$today+".txt"
$fullPath= "$MyDir\$fileName"

Write-Host "Attention TJ about to create $($fullPath) ..."

New-Item -Path $fullPath -ItemType File

Start-Sleep -Seconds 1

#open file
codium $fullPath

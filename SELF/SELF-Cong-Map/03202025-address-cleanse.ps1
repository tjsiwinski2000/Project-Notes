<#
03-20-2025

#>

$s= Get-Content C:\Users\TJ\source\repos\Project-Notes\SELF-Cong-Map\addresses.csv

$outFile=New-Item -Force -Path  C:\Users\TJ\source\repos\Project-Notes\SELF-Cong-Map\addresses-cleansed.csv

foreach ($line in $s)
{
    if ($line.length)
    {
            $line=$line.TrimEnd(" ")
            if ($line.EndsWith(";")) {$line=$line.Substring(0,$line.Length-1)}
            add-content -Path $outFile -Value $line
    }
}
<# 
0305-2025 Cleansing file test
#>

$s= Get-Content 'C:\Users\TJ\Downloads\addressInput.txt'

# create new output file
$outFile= New-Item -Force -Path C:\Users\TJ\source\repos\Project-Notes\SELF-Cong-Map\addresses.csv
Set-Content -Path $outFile -Value "NAME;STREET;CITY"

# declare, initialize vars
$count=0
$regex='\(?(?<areaCode>\d{3})\)?(-| )?(?<first>\d{3})(-| )?(?<second>\d{4})'
$bPhone = [bool] $false
$outLine=""
#boolean to skip next line due to repeated names
$bSkip =[bool]$false
foreach ($line in $s)
{
    $count +=1
    # Account for real data starts line 6
    if ($count -gt 6)
    { 
        if ($bSkip -eq $false)
        {
        if ($line -match $regex){$bPhone = [bool]$true} else {$bPhone = [bool]$false}
            #Ignore e-mail and phone 
            if  ( ($line -notmatch "@") -and ($bPhone -eq $false))
            {
                #Write-Host $line
                if ($line -match "TX")
                {
                    # logic to skip next line
                    # add new line to outline
                    $outLine=$outLine + ";" + $line + "`r"
                    Write-Host $outLine
                    Add-Content -Path $outFile -Value $outLine
                    $outLine=""
                    $bSkip = [bool]$true
                }
                else
                {
                    if ($outLine.Length) 
                    {
                        $outLine= $outLine +";" + $line 
                    }
                    else
                    {
                        $outLine=  $line        
                    }
                } #else
            } #phone , email match
        } #bSkip
        else
        {
            $bSkip = [bool]$false
        }
    }#count gt 6
}#for

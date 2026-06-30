# 02072025 for Math Practice
$timeStart= get-date
$timeDiff =0
$totalCorrectAnswers=0
$totalOopsAnswers=0

while ($timeDiff -lt 10){
    $number1 = Get-Random -Minimum -10 -Maximum 10
    $number2 = Get-Random -Minimum -10 -Maximum 10
    $correctAnswer= $number1 * $number2
    $presentProblem= "$number1 X $number2"
  
    $studentAnswer= Read-Host $presentProblem
    if ($studentAnswer -eq $correctAnswer)
    {
        write-Host "Correct $presentProblem  equals  $studentAnswer"
        [System.Console]::Beep(340, 500) 
        $totalCorrectAnswers +=1
    }
    else
    {
        write-Host "OOPs $presentProblem  DOES NOT equal  $studentAnswer"
        [System.Console]::Beep(840, 500) 
        $totalOopsAnswers +=1
    }
   
    $timeNow =get-date
    #$timeDiff= new-timespan -start $timeStart -end $timeNow
    $timeDiff= ( $timeNow -$timeStart).TotalSeconds
}
$timeDiff=$timeDiff.ToString('00.0')
write-Host "$timeDiff seconds has passed"
$TotalAnswers= $totalOopsAnswers + $totalCorrectAnswers
write-host " $totalCorrectAnswers correct answers out of $TotalAnswers"
write-host "THANK YOU FOR PLAYING "
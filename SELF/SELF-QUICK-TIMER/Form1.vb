Public Class Form1

    ' This event handler is triggered every time the timer "ticks" (every 1 second).
    Private Sub myActualTime_Tick(sender As Object, e As EventArgs) Handles myActualTime.Tick
        ' Update the Text property of the timeLabel with the current time.
        ' DateTime.Now gets the current date and time.
        ' ToLongTimeString() formats the time as a long string (e.g., 10:30:45 AM).
        timeLabel.Text = DateTime.Now.ToLongTimeString()
    End Sub

    ' This event handler runs when the form first loads.
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ' This is a good place to start the timer, if it's not already enabled.
        myActualTime.Start()
    End Sub
    ' Declare a Stopwatch object at the form level to track elapsed time.
    Private myStopwatch As New Stopwatch()

    Private Sub startButton_Click(sender As Object, e As EventArgs) Handles startButton.Click
        ' Start the stopwatch and enable the timer to start updating the label.
        myStopwatch.Start()
        myTimer.Enabled = True
    End Sub

    Private Sub stopButton_Click(sender As Object, e As EventArgs) Handles stopButton.Click
        ' Stop the stopwatch and disable the timer.
        myStopwatch.Stop()
        myTimer.Enabled = False
    End Sub

    Private Sub resetButton_Click(sender As Object, e As EventArgs) Handles resetButton.Click
        ' Stop the timer and reset the stopwatch.
        myStopwatch.Stop()
        myStopwatch.Reset()
        myTimer.Enabled = False

        ' Update the label to show a reset state.
        elapsedTimeLabel.Text = "00:00:00"
    End Sub

    Private Sub myTimer_Tick(sender As Object, e As EventArgs) Handles myTimer.Tick, myActualTime.Tick
        ' This event is triggered repeatedly by the timer.
        ' It updates the label with the current elapsed time from the stopwatch.

        ' Format the elapsed time to show hours, minutes, seconds, and milliseconds.
        ' The {0:00} format specifier ensures two digits are always shown (e.g., 01, 09, 10).
        Dim formattedTime As String = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
                                                     myStopwatch.Elapsed.Hours,
                                                     myStopwatch.Elapsed.Minutes,
                                                     myStopwatch.Elapsed.Seconds,
                                                     myStopwatch.Elapsed.Milliseconds \ 10) ' Milliseconds divided by 10 for two digits

        elapsedTimeLabel.Text = formattedTime
    End Sub
End Class
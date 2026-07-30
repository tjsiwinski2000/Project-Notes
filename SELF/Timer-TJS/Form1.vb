Public Class Form1

    Private WithEvents CountdownTimer As New Timer()
    Private totalSeconds As Integer
    Private secondsRemaining As Integer
    Private ReadOnly warningThreshold As Double = 0.1 ' 10%

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Me.TopMost = True
        Dim x As Integer = Screen.PrimaryScreen.WorkingArea.Width - Me.Width
        Dim y As Integer = 0
        Me.Location = New Point(x, y)
        Dim minutes As Integer = 30   ' <-- change starting minutes here
        totalSeconds = minutes * 60
        secondsRemaining = totalSeconds

        UpdateDisplay()

        CountdownTimer.Interval = 1000 ' 1 second
        CountdownTimer.Start()
    End Sub

    Private Sub CountdownTimer_Tick(sender As Object, e As EventArgs) Handles CountdownTimer.Tick
        secondsRemaining -= 1

        If secondsRemaining <= 0 Then
            secondsRemaining = 0
            CountdownTimer.Stop()
        End If

        UpdateDisplay()
        CheckWarningState()

        If secondsRemaining = 0 Then
            MessageBox.Show("Time's up!", "Timer", MessageBoxButtons.OK, MessageBoxIcon.Warning)
            Beep()
            Beep()
            Beep()
        End If
    End Sub

    Private Sub UpdateDisplay()
        Dim ts As TimeSpan = TimeSpan.FromSeconds(secondsRemaining)
        Label1.Text = ts.ToString("mm\:ss")
    End Sub

    Private Sub CheckWarningState()
        Dim fractionRemaining As Double = CDbl(secondsRemaining) / CDbl(totalSeconds)

        If fractionRemaining <= warningThreshold Then
            Me.BackColor = Color.Red
            Label1.BackColor = Color.Red
            Label1.ForeColor = Color.White
        Else
            Me.BackColor = SystemColors.Control
            Label1.BackColor = SystemColors.Control
            Label1.ForeColor = Color.Black
        End If
    End Sub

    Private Sub Form1_MouseDoubleClick(sender As Object, e As MouseEventArgs) Handles Me.MouseDoubleClick
        Form1_Load(Me, EventArgs.Empty)
        Beep()
    End Sub
End Class
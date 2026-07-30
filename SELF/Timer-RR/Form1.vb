Public Class Timer_RR_Form1
    Inherits Form

    Private WithEvents CountdownTimer As New Timer()
    Private totalSeconds As Integer
    Private secondsRemaining As Integer
    Private ReadOnly warningThreshold As Double = 0.1

    Private WithEvents lblTime As New Label()

    Public Sub New()
        Me.TopMost = True
        Me.Text = "Countdown"
        Me.Width = 250
        Me.Height = 120
        Me.StartPosition = FormStartPosition.CenterScreen

        Dim minutes As Integer = 5
        totalSeconds = minutes * 60
        secondsRemaining = totalSeconds

        lblTime.Dock = DockStyle.Fill
        lblTime.TextAlign = ContentAlignment.MiddleCenter
        lblTime.Font = New Font("Segoe UI", 28, FontStyle.Bold)
        Me.Controls.Add(lblTime)

        UpdateDisplay()

        CountdownTimer.Interval = 1000
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
        End If
    End Sub

    Private Sub UpdateDisplay()
        Dim ts As TimeSpan = TimeSpan.FromSeconds(secondsRemaining)
        lblTime.Text = ts.ToString("mm\:ss")
    End Sub

    Private Sub CheckWarningState()
        Dim fractionRemaining As Double = CDbl(secondsRemaining) / CDbl(totalSeconds)

        If fractionRemaining <= warningThreshold Then
            Me.BackColor = Color.Red
            lblTime.BackColor = Color.Red
            lblTime.ForeColor = Color.White
        Else
            Me.BackColor = SystemColors.Control
            lblTime.BackColor = SystemColors.Control
            lblTime.ForeColor = Color.Black
        End If
    End Sub

End Class
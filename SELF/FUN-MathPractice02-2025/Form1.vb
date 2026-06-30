Imports System.Reflection

Public Class Form1
    Dim Answer As Int16
    Dim CorrectAnswers As Int16
    Dim WrongAnswers As Int16
    Dim TotalAnswers As Int16
    Dim counter As Int16

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        DetermineNextProblem()
        CorrectAnswers = 0
        WrongAnswers = 0
        Timer1.Interval = 1000
        Timer1.Start()
    End Sub

    Function DetermineNextProblem()
        Dim Number1 As Int16
        Dim Number2 As Int16

        'create two random numbes 1-20
        Number1 = CInt(Math.Ceiling(Rnd() * 20)) + 1
        Number2 = CInt(Math.Ceiling(Rnd() * 20)) + 1

        'subtract 10 from each to get -10 to 10
        Number1 -= 10
        Number2 -= 10
        Answer = Number1 * Number2
        TextBox1.Text = ""
        Label1.Text = Number1.ToString() + "  X  " + Number2.ToString()
    End Function

    Function Evaluate()
        Dim InputAnswer As Int16
        InputAnswer = TextBox1.Text


        If InputAnswer = Answer Then
            Me.Text = "correct"
            TextBox2.Text = TextBox2.Text + vbCrLf + "YES " + Label1.Text + " = " + TextBox1.Text
            CorrectAnswers += 1
            Beep()
            Beep()
        Else
            Me.Text = "incorrect"
            TextBox2.Text = TextBox2.Text + vbCrLf + " oops " + Label1.Text + " not equal " + TextBox1.Text
            WrongAnswers += 1
        End If
        TotalAnswers = CorrectAnswers + WrongAnswers
        Me.Text = CorrectAnswers.ToString() + " correct || " + WrongAnswers.ToString() + " incorrect || " + TotalAnswers.ToString() + " total answers"

        DetermineNextProblem()
    End Function
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Evaluate()
    End Sub


    Private Sub TextBox1_KeyPress(sender As Object, e As KeyPressEventArgs) Handles TextBox1.KeyPress
        If e.KeyChar = Microsoft.VisualBasic.ChrW(Keys.Return) Then
            Evaluate()
        End If
    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        counter = counter + 1
        Dim secondsleft As Int16
        secondsleft = 30 - counter
        Label2.Text = secondsleft
        If secondsleft < 1 Then
            Button1.Enabled = False
            TextBox1.Enabled = False
            Me.Text = Me.Text + " *** THANK YOU FOR PLAYING ***"
            Timer1.Stop()
        End If
    End Sub
End Class

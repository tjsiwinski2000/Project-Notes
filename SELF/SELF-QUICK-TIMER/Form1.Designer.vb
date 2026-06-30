<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form1))
        Me.myActualTime = New System.Windows.Forms.Timer(Me.components)
        Me.timeLabel = New System.Windows.Forms.Label()
        Me.elapsedTimeLabel = New System.Windows.Forms.Label()
        Me.startButton = New System.Windows.Forms.Button()
        Me.stopButton = New System.Windows.Forms.Button()
        Me.resetButton = New System.Windows.Forms.Button()
        Me.myTimer = New System.Windows.Forms.Timer(Me.components)
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'myActualTime
        '
        Me.myActualTime.Enabled = True
        Me.myActualTime.Interval = 1000
        '
        'timeLabel
        '
        Me.timeLabel.AutoSize = True
        Me.timeLabel.Font = New System.Drawing.Font("Microsoft Sans Serif", 15.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.timeLabel.Location = New System.Drawing.Point(-2, -1)
        Me.timeLabel.Name = "timeLabel"
        Me.timeLabel.Size = New System.Drawing.Size(105, 25)
        Me.timeLabel.TabIndex = 1
        Me.timeLabel.Text = "timeLabel"
        '
        'elapsedTimeLabel
        '
        Me.elapsedTimeLabel.AutoSize = True
        Me.elapsedTimeLabel.Font = New System.Drawing.Font("Microsoft Sans Serif", 15.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.elapsedTimeLabel.Location = New System.Drawing.Point(118, -1)
        Me.elapsedTimeLabel.Name = "elapsedTimeLabel"
        Me.elapsedTimeLabel.Size = New System.Drawing.Size(188, 25)
        Me.elapsedTimeLabel.TabIndex = 2
        Me.elapsedTimeLabel.Text = "elapsedTimeLabel"
        '
        'startButton
        '
        Me.startButton.Location = New System.Drawing.Point(12, 27)
        Me.startButton.Name = "startButton"
        Me.startButton.Size = New System.Drawing.Size(75, 23)
        Me.startButton.TabIndex = 3
        Me.startButton.Text = "START"
        Me.startButton.UseVisualStyleBackColor = True
        '
        'stopButton
        '
        Me.stopButton.Location = New System.Drawing.Point(93, 27)
        Me.stopButton.Name = "stopButton"
        Me.stopButton.Size = New System.Drawing.Size(75, 23)
        Me.stopButton.TabIndex = 4
        Me.stopButton.Text = "STOP"
        Me.stopButton.UseVisualStyleBackColor = True
        '
        'resetButton
        '
        Me.resetButton.Location = New System.Drawing.Point(174, 27)
        Me.resetButton.Name = "resetButton"
        Me.resetButton.Size = New System.Drawing.Size(75, 23)
        Me.resetButton.TabIndex = 5
        Me.resetButton.Text = "RESET"
        Me.resetButton.UseVisualStyleBackColor = True
        '
        'myTimer
        '
        '
        'PictureBox1
        '
        Me.PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), System.Drawing.Image)
        Me.PictureBox1.InitialImage = CType(resources.GetObject("PictureBox1.InitialImage"), System.Drawing.Image)
        Me.PictureBox1.Location = New System.Drawing.Point(12, 56)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(281, 175)
        Me.PictureBox1.TabIndex = 6
        Me.PictureBox1.TabStop = False
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(302, 256)
        Me.Controls.Add(Me.PictureBox1)
        Me.Controls.Add(Me.resetButton)
        Me.Controls.Add(Me.stopButton)
        Me.Controls.Add(Me.startButton)
        Me.Controls.Add(Me.elapsedTimeLabel)
        Me.Controls.Add(Me.timeLabel)
        Me.Name = "Form1"
        Me.Text = "QUICK TIME"
        Me.TopMost = True
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents myActualTime As Timer
    Friend WithEvents timeLabel As Label
    Friend WithEvents elapsedTimeLabel As Label
    Friend WithEvents startButton As Button
    Friend WithEvents stopButton As Button
    Friend WithEvents resetButton As Button
    Friend WithEvents myTimer As Timer
    Friend WithEvents PictureBox1 As PictureBox
End Class

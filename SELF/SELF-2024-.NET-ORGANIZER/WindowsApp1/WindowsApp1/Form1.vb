Imports System.CodeDom.Compiler
Imports System.IO
Imports System.Runtime.CompilerServices
Imports System.Runtime.Remoting.Channels
Imports System.Runtime.Remoting.Messaging
Imports System.Runtime.Serialization
Imports System.Windows.Forms.VisualStyles.VisualStyleElement
Imports Newtonsoft.Json.Linq

Public Class Form1
    Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ComboBox1.SelectedIndexChanged
        Dim s As String
        Clipboard.Clear()
        Clipboard.SetText(ComboBox1.Text)

    End Sub

    Private Sub PictureBox1_Click(sender As Object, e As EventArgs) Handles PictureBox1.Click
        PictureBox2.Visible = True
        Me.Width = 1177
        Me.Height = 465


    End Sub

    Private Sub ListBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ListBox1.SelectedIndexChanged
        If ListBox1.Text = "MSPaint" Then
            Process.Start("MSPaint")
        ElseIf ListBox1.Text = "Notepad++" Then
            Process.Start("C:\Program Files\Notepad++\notepad++.exe")
        ElseIf ListBox1.Text = "Chrome" Then
            Process.Start("C:\Program Files\Google\Chrome\Application\chrome.exe")
        End If
    End Sub

    Private Sub ListBox2_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ListBox2.SelectedIndexChanged
        Clipboard.Clear()
        Clipboard.SetText(ListBox2.Text)
    End Sub


    Private Sub Get_Weather()
        Dim webClient As New System.Net.WebClient
        Dim Response
        Try
            'Pull Weather JSON from Weather API, note hard coded key and location
            Dim result As String = webClient.DownloadString("http://api.weatherapi.com/v1/current.json?key=02d8de7fa6594eefb81213151242011&q=78247&aqi=no")
            'TextBox1.Text = result

            'Utilize JObject part of [Newtonsoft.Json.Linq] to 
            Dim parsejson As JObject = JObject.Parse(result)

            'Parse JSON to pull back [current]; [current] contains temperature
            Dim current = parsejson.SelectToken("current").ToString()

            'Parse [current] for [temp_f], temperature in Fahrenheit
            Dim parsejson2 As JObject = JObject.Parse(current)
            Dim temp_f = parsejson2.SelectToken("temp_f").ToString()
            'Me.Text = "Current Temperature in San Antonio is " + temp_f + " Fahrenheit"
            Label1.Text = "Current Temp is " + temp_f + " F"

            'Parse [current] for [condition] and then [icon]
            Dim condition = parsejson2.SelectToken("condition").ToString()
            Dim parsejson3 As JObject = JObject.Parse(condition)
            Dim icon_url = parsejson3.SelectToken("icon").ToString()
            icon_url = "https:" + icon_url
            'Download current weather condition image to an [in-memory stream].
            Dim tImage As Bitmap = Bitmap.FromStream(New MemoryStream(webClient.DownloadData(icon_url)))
            PB_Weather.Image = tImage

        Catch ex As System.Net.WebException
            Dim s As String
            s = ex.ToString()
            Response = MsgBox("ugh API error occured " + s, vbOK, "oh shucks")
        End Try
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles Me.Load
        Get_Weather()
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Get_Weather()
    End Sub

    Private Sub PictureBox2_Click(sender As Object, e As EventArgs) Handles PictureBox2.Click
        PictureBox2.Visible = False
        Me.Width = 245
        Me.Height = 235
    End Sub

    Private Sub PictureBox1_ClientSizeChanged(sender As Object, e As EventArgs) Handles PictureBox1.ClientSizeChanged

    End Sub
End Class

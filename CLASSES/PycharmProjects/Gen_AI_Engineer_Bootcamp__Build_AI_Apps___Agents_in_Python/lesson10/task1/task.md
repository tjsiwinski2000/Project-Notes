# Fix the Automation Script

This script monitors a Google Spreadsheet for new rows, summarises them using an AI model, and emails the summary to a recipient automatically. It reads the last processed row number from `last_row.txt`, processes only the new rows, then updates `last_row.txt` so the next run starts from where it left off.

The starter code has two mistakes. Fix them:

1. The environment variable for the Gemini API key is wrong. Change `"GOOGLE_API_KEY"` to `"GEMINI_API_KEY"` in `summarize_with_ai`.
2. The SMTP port is wrong. Change `SMTP_PORT = 465` to `SMTP_PORT = 587`.

**Important:** Fill in all the values in the `.env` file before running the script. You will need a Google Sheets API key, your spreadsheet ID, a Gmail address with an app password, and a Gemini API key.

<div class="hint">

`SMTP_PORT 587` is used for Gmail's STARTTLS connection, which matches the `server.starttls()` call in `send_email`.

</div>

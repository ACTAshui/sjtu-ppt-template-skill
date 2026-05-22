# Office Compatibility

Use this when a generated or revised deck must be verified in a local presentation application.

## Engine Order

Prefer the first available local engine:

1. Microsoft PowerPoint desktop COM: `PowerPoint.Application`.
2. WPS Presentation COM: `KWPP.Application`.
3. LibreOffice command line as a render/repair fallback.

Do not assume Microsoft PowerPoint desktop is installed just because `PowerPoint.Application` resolves. Confirm that COM can create an application instance and open the file.

## Validation Rules

Before telling the user that a PPTX opens:

- Open the file in the selected local engine.
- Read the slide count.
- Close the document cleanly.
- Remove inherited read-only attributes on generated copies.
- Prefer a short ASCII output path for compatibility handoff when the user reports open failures.

If PowerPoint COM returns `RPC_E_CALL_REJECTED`, check whether desktop PowerPoint is actually installed and registered. On systems with only Microsoft 365 Hub, WPS, or LibreOffice, use WPS/LibreOffice for validation instead of repeatedly calling PowerPoint COM.

## Repair Workflow

When a PPTX fails to open for the user:

1. Return to the latest user-provided base file.
2. Copy it to a short path such as the desktop.
3. Clear `ReadOnly` and unblock the file.
4. Validate with `scripts/office_bridge.ps1`.
5. If needed, re-save through WPS with `SaveAs(..., 24)`.
6. Generate a PDF fallback for immediate presentation.

Example:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/office_bridge.ps1 `
  -InputPptx "C:\Users\lenovo\Desktop\deck.pptx" `
  -OutputPptx "C:\Users\lenovo\Desktop\deck_wps_saved.pptx" `
  -Engine auto `
  -Visible
```

Record which engine actually opened the deck in the final response.

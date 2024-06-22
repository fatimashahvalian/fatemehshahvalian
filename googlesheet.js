function doGet() {
    return HtmlService.createHtmlOutputFromFile('Index');
  }
  
  function addContact(name, phone, email) {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    sheet.appendRow([name, phone, email]);
    return "Contact added successfully";
  }
  
  function getContacts() {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = sheet.getDataRange().getValues();
    return data;
  }
  
  function deleteContact(row) {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    sheet.deleteRow(row);
    return "Contact deleted successfully";
  }
  
  function editContact(row, name, phone, email) {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    sheet.getRange(row, 1).setValue(name);
    sheet.getRange(row, 2).setValue(phone);
    sheet.getRange(row, 3).setValue(email);
    return "Contact edited successfully";
  }
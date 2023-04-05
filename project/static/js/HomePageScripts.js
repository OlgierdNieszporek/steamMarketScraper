function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  document.getElementByXpath
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementsByTagName('table')[0];
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
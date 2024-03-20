<script> 
function fnMoveItems(lstbxFrom, lstbxTo) {
  var varFromBox = document.getElementById(lstbxFrom);
  var varToBox = document.getElementById(lstbxTo);

  if (varFromBox !== null && varToBox !== null) {
    if (varFromBox.options.length < 1) {
      alert('There are no items in the source ListBox');
      return false;
    }

    if (varFromBox.selectedIndex === -1) {
      alert('Please select an Item to move');
      return false;
    }

    while (varFromBox.selectedIndex >= 0) {
      var selectedOption = varFromBox.options[varFromBox.selectedIndex];
      var newOption = new Option(selectedOption.text, selectedOption.value);
      varToBox.add(newOption);
      varFromBox.remove(varFromBox.selectedIndex);
    }
  }

  return false;
}
</script>

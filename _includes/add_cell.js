function add_code_cell(div)
{
  var ele = document.createElement("pre");
  ele.setAttribute("data-executable", "true");
  ele.setAttribute("data-language", "python");
  document.getElementById(div).appendChild(ele);
}
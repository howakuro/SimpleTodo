"use strict";

var id_state_elem = document.getElementById("id_state");

id_state_elem.classList.add("btn-group");
id_state_elem.classList.add("btn-group-toggle");
id_state_elem.classList.add("w-100")
id_state_elem.setAttribute("data-toggle", "buttons");

var children = id_state_elem.childNodes;
for (const node of children) {
    if (node.nodeType === Node.ELEMENT_NODE) {
      // nodeに対応する要素に背景色をつける
      node.classList.add("btn");
      node.classList.add("btn-secondary");
      node.classList.add("w-auto");
      var input_elem = node.getElementsByTagName("input");
      console.log(node.querySelector(":checked"));
      if(node.querySelector(":checked") !== null){
        node.classList.add("active");
      }
}}
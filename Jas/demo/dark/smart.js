var smart = document.getElementById('Smart_Div');

var Original_Scontent = `
<div class="row">
<div class="col-md-8 col-md-offset-2 text-center heading">
   <div class="header-page">
      <h2>Smart Interaction</h2>

   </div>

   <span class="heading-meta-sub">Smart Interaction</span>
   <!-- </br> -->
   <p>Where User Can Modify Existing Data With One Click</p>
</div>

<div class="row">
   <div class="col-md-4">
      <div class="blog">
         <input style="color:black" type="text" id="input" placeholder="Enter Data">
         <button id="AddData" class="btn btn" onclick="Add_Data()">Add Data</a></button>

         <select style="color:black" value="">

            <option value="" disabled selected hidden>Show Data</option>
            <option id="Fir">test1</option>

         </select>
      </div>
   </div>
 </div>
</div>`
function Getname() {
   fetch('http://localhost:3000/Data')
      .then(response => response.json())
      .then(json => {
         //.Services
         json.forEach(element => {
            var Scontent = Original_Scontent;
            Scontent = Scontent.replace('Test Number', element.A)
            //Scontent = Scontent.replace('Description',element.B)

            var smarttt = document.createElement('S_Div')
            smarttt.innerHTML = Scontent
            smarttt.className = "col-md-8 col-md-offset-2 text-center heading";
            smart.appendChild(smarttt)
         });
      });
};


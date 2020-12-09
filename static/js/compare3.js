function compareHandle() {
    const checkboxes = document.getElementsByClassName("comparecb");
    let cb1, cb2;
    for (let i = 0; i < checkboxes.length; i++) {
      console.log(checkboxes[i].checked);
      if (checkboxes[i].checked && cb1 === undefined) {
        cb1 = checkboxes[i];
      } else if (checkboxes[i].checked && cb2 === undefined) {
        cb2 = checkboxes[i];
      } else if (cb1 && cb2 && checkboxes[i].checked) {
        alert("Please check any two checkboxes");
        // return;
        break;
      }
    }
    console.log("CHECKBOXES", checkboxes);
    console.log("CHECKBOX1", cb1.name);
    console.log("CHECKBOX2", cb2.name);
  
    $.ajax({
      type: "GET",
      url: "http://127.0.0.1:8000/property/compare/",
      data: {
        id1: cb1.name,
        id2: cb2.name,
      },
      success: function (response) {
        console.log(response);
        console.log("http://127.0.0.1:8000/media/"+response[2].fields.Kitchen_Image);
        
        if (response[0] && response[1]){
          document.getElementById('container1').style.display='block';
          document.getElementById('container2').style.display='none';
          document.getElementById('divc1').style.display='block';
          document.getElementById('container4').style.display='none';
          document.getElementById('price1').innerText=response[0].fields.price;
          document.getElementById('price2').innerText=response[1].fields.price;
          document.getElementById('area1').innerText=response[0].fields.area;
          document.getElementById('area2').innerText=response[1].fields.area;
          document.getElementById('age1').innerText=response[0].fields.age_of_house;
          document.getElementById('age2').innerText=response[1].fields.age_of_house;
          document.getElementById('br1').innerText=response[0].fields.no_of_bedrooms;
          document.getElementById('br2').innerText=response[1].fields.no_of_bedrooms;
          document.getElementById('type1').innerText=response[0].fields.type_house;
          document.getElementById('type2').innerText=response[1].fields.type_house;
          document.getElementById('f1').innerText=response[0].fields.no_of_floors;
          document.getElementById('f2').innerText=response[1].fields.no_of_floors;
          document.getElementById('pname1').innerText=response[0].fields.name;
          document.getElementById('pname2').innerText=response[1].fields.name;
          document.getElementById('pos1').innerText=response[0].fields.possession;
          document.getElementById('pos2').innerText=response[1].fields.possession;
          document.getElementById('kitchenimg1').src = "../../media/"+response[2].fields.Kitchen_Image;
          document.getElementById('kitchenimg2').src = "../../media/"+response[3].fields.Kitchen_Image;
          document.getElementById('lrimg1').src = "../../media/"+response[2].fields.LivingRoom_Image;
          document.getElementById('lrimg2').src = "../../media/"+response[3].fields.LivingRoom_Image;

          // document.getElementById('img1').style.width='100px';
          // document.getElementById('img1').style.height='80px';

          if (response[0].fields.Gym==true){
            document.getElementById('gym1').innerText='Yes';
          }else{
            document.getElementById('gym1').innerText='No';
          }
          if (response[1].fields.Gym==true){
            document.getElementById('gym2').innerText='Yes';
          }else{
            document.getElementById('gym2').innerText='No';
          }
          if (response[0].fields.swimming_pool==true){
            document.getElementById('swp1').innerText='Yes';
          }else{
            document.getElementById('swp1').innerText='No';
          }
          if (response[1].fields.swimming_pool==true){
            document.getElementById('swp2').innerText='Yes';
          }else{
            document.getElementById('swp2').innerText='No';
          }
          if (response[0].fields.Conference_room==true){
            document.getElementById('cr1').innerText='Yes';
          }else{
            document.getElementById('cr1').innerText='No';
          }
          if (response[1].fields.Conference_room==true){
            document.getElementById('cr2').innerText='Yes';
          }else{
            document.getElementById('cr2').innerText='No';
          }
          if (response[0].fields.Parking==true){
            document.getElementById('park1').innerText='Yes';
          }else{
            document.getElementById('park1').innerText='No';
          }
          if (response[1].fields.Parking==true){
            document.getElementById('park2').innerText='Yes';
          }else{
            document.getElementById('park2').innerText='No';
          }
        }
        
        console.log("compare successfull");
      },
    });
  }
  
  function compareHandle1(){
    document.getElementById('container1').style.display='none';
    document.getElementById('container2').style.display='block';
    document.getElementById('divc1').style.display='none';
    document.getElementById('container4').style.display='block';
  }
  
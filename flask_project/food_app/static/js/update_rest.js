const myForm = document.getElementById("photoSubm");
const photo_btn = document.getElementById('photo_up_btn');
const inpFile_photo=document.getElementById("fileInput");
//const prev_container=document.getElementById("imagePreview");
//const image_prev=prev_container.querySelector(".img_preview");
const popup_cover = $('#exampleModalCenter');
const popup_dish =$('#exampleModalCenter1');
const btn_upload_cover=document.getElementById("btnUpload");

const btn_upload_menu=document.getElementById("btnUploadMenu");
const btn_add_dish = document.getElementById("dishAdd");

let file=null;
photo_btn.addEventListener('click', () => {
    document.getElementById('fileInput').click();
});
btn_add_dish.addEventListener('click', () => {
    console.log("Clicked");
    popup_dish.modal('show');
});

function cleanImageDisplay(body_element)
{
    while(body_element.firstChild){
        body_element.removeChild(body_element.firstChild);
    }
}

function fillModalViewImages(body_element,files){

    cleanImageDisplay(body_element);
    if(files.length === 0)
    {
        const para = document.createElement('p');
        para.textContent = 'No files currently selected for upload';
        body_element.appendChild(para);
    }
    else{
        const list = document.createElement('ol');
        body_element.appendChild(list);

        for(const file of files) {
            const list_item = document.createElement('li');
            const para = document.createElement('p');
            para.textContent = `File name ${file.name}.`;
            const image = document.createElement('img');
            image.src = URL.createObjectURL(file);
            image.style.height='80px';
            list_item.appendChild(image);
            list_item.appendChild(para);
            list.appendChild(list_item);
        }
    }
}




inpFile_photo.addEventListener("change",function(){
    file = this.files;
    if (file){
        let photo_modal_body=document.getElementById("photoModalBody");
        fillModalViewImages(photo_modal_body,file);
        popup_cover.modal('show');
    }
})

function sendData(url_string,dataFormat,process_data,c_type,callback){
    $.ajax({
        type: 'POST',
        url: url_string ,
        data:dataFormat,
        processData: false,
        contentType: false,
        //contentType: "multipart/form-data",
        success: function(data)
        {
            window.alert("Sent");
        }
    });
}
btn_upload_cover.addEventListener('click', () => {
    var fileFormData = new FormData();
    if (file){
        for ( const ele of  file){
            console.log(ele)
            fileFormData.append("files[]",ele);
        }
        for (var pair of fileFormData.entries()) {
            console.log(pair[0]+ ', ' + pair[1].files); 
        }
        sendData("/api/add/cover",fileFormData,false,false,false);
    }
    
})
btn_upload_menu.addEventListener('click',function(){
    var menuForm = document.getElementById("menuForm");
    var blockRestaurant = document.querySelector(".container.mt-4");
    var id = blockRestaurant.dataset.id
    var menuFormData = new FormData(menuForm);
    menuFormData.append("id",id)
    for (var pair of menuFormData.entries()) {
        console.log(pair[0]+ ', ' + pair[1]); 
    }
    if(menuFormData.get("dish_name") && menuFormData.get("dish_option"))
    {
        sendData("/api/add/dish",menuFormData,false,false,false);
    }
    
})
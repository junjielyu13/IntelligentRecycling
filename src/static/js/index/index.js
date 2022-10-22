let video = document.getElementById("video");

function getMedia() {
  let contraints = {
    video: { width: 640, height: 360 },
    audio: false,
  };

  let promise = navigator.mediaDevices.getUserMedia(contraints);
  promise
    .then(function (mediaStream) {
      video.srcObject = mediaStream;
      video.play();
    })
    .catch(function (error) {
      console.log(error);
    });
}

function takePhoto() {
  let canvas = document.getElementById("canvas");
  let ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0, 640, 360);
}

function Download() {
  let type = "jpg";
  var imgdata = canvas.toDataURL(type);

  var fixtype = function (type) {
    type = type.toLocaleLowerCase().replace(/jpg/i, "jpeg");
    var r = type.match(/png|jpeg|bmp|gif/)[0];
    return "image/" + r;
  };

  imgdata = imgdata.replace(fixtype(type), "image/octet-stream");

  var savaFile = function (data, filename) {
    var save_link = document.createElementNS(
      "http://www.w3.org/1999/xhtml",
      "a"
    );
    save_link.href = data;
    save_link.download = filename;

    var event = document.createEvent("MouseEvents");
    event.initMouseEvent(
      "click",
      true,
      false,
      window,
      0,
      0,
      0,
      0,
      0,
      false,
      false,
      false,
      false,
      0,
      null
    );
    save_link.dispatchEvent(event);
  };

  let result = Math.floor(Math.random() * 99999999);

  let filename = "img_" + new Date().getSeconds() + result + "." + type;

  savaFile(imgdata, filename);

  display = document.querySelector(".present");
  display.style.display = "block";

  $.ajax({
    type: "POST",

    url: "/identify",

    data: { name: filename },

    dataType: "json",

    success: function (data) {
      console.log("success");
      console.log(data);

      var imgbox = document.querySelector("#info-img");
      var infor_titile = document.querySelector("#info-title");
      var infor_1 = document.querySelector("#info-1");
      var infor_2 = document.querySelector("#info-2");
      var infor_3 = document.querySelector("#info-3");

      if (data.result === "amarillo") {
        imgbox.src = "../static/upload/contenidor_groc.png";

        infor_titile.innerHTML = "CONTENEDOR AMARILLO - ENVASES";

        infor_1.innerHTML =
          "envases de plástico, latas de bebidas y conservas, briks, chapas y tapas de metal, papel de aluminio y film transparente, bandejas de porexpán, etc.";

        infor_2.innerHTML =
          "juguetes, mangueras de regar, tubos, materiales como cintas de vídeo y CDs, y envases de productos peligrosos (disolventes o pinturas), etc.";

        infor_3.innerHTML =
          "Los envases se llevan a las plantas de triaje, donde se separan los distintos materiales mediante la combinación de técnicas ópticas, mecánicas y manuales. Los distintos materiales seleccionados son compactados, embalados y distribuidos en los centros de selección.";
      } else if (data.result === "azul") {
        imgbox.src = "../static/upload/contenidor_blau.png";

        infor_titile.innerHTML = "CONTENEDOR AZUL -PAPEL Y CARTRÓN";

        infor_1.innerHTML =
          "envases y cajas de cartón, periódicos, revistas, libretas sin espiral metálica, sobres, bolsas de papel, folios, papel de regalo, etc.";

        infor_2.innerHTML =
          "papel y material sucio, como servilletas de papel o papel de cocina manchados de aceite, que van al contenedor marrón. Los briks y el papel de aluminio van al contenedor amarillo.";

        infor_3.innerHTML =
          "Los residuos recogidos en el contenedor azul se llevan a las plantas de reciclaje, donde se convierten en grandes balas de papel triturado. Estas balas se ponen a remojo para obtener pasta de papel, que se cuela para filtrar los materiales férricos. La pasta resultante se seca, plancha y se hacen bobinas, que se distribuyen en las fábricas papeleras para tener una nueva vida útil.";
      } else if (data.result === "marron") {
        imgbox.src = "../static/upload/contenidor_marro.png";

        infor_titile.innerHTML = "CONTENEDOR MARRÓN - ORGÁNICA";

        infor_1.innerHTML =
          "restos de carne, pescado, pan, fruta, verdura, marisco, cáscaras de huevo y de frutos secos, tapones de corcho, bolsas de infusión, marrón del café, papel de cocina y servilletas manchadas de aceite, restos de jardinería, etc.";

        infor_2.innerHTML =
          "restos de barrer, pelo, pañales y heces de animales, que van al contenedor gris.";

        infor_3.innerHTML =
          "Los residuos de origen vegetal y/o animal son susceptibles de degradarse biológicamente, como los restos de comida y jardinería. Es una fracción de residuos muy relevante, puesto que constituye la tercera parte de los residuos que generamos en nuestro hogar. Estos residuos se llevan a los ecoparques, donde se convierten en compost y biogás.";
      } else if (data.result === "verde") {
        imgbox.src = "../static/upload/contenidor_verd.png";

        infor_titile.innerHTML = "CONTENEDOR VERDE - VIDRIO";

        infor_1.innerHTML =
          "envases y botellas de vidrio, sin tapones ni tapas.";

        infor_2.innerHTML =
          "vasos rotos, cristales planos, espejos, restos de cerámica, platos, bombillas, fluorescentes, etc.";

        infor_3.innerHTML =
          "El vidrio recogido se lleva a la planta de reciclaje, donde se limpia, se extraen los materiales férricos con unos imanes y se tritura hasta convertirlo en polvo (cristal seleccionado, limpio y molido), que permite fabricar envases de vidrio exactamente iguales que los originales para hacer botellas, botes o bombillas, entre otros.";
      } else {
        imgbox.src = "../static/upload/contenidor_gris.png";

        infor_titile.innerHTML = "CONTENEDOR GRIS - DESECHO";

        infor_1.innerHTML =
          "colillas, compresas, pañales, restos de barrer, algodón, pelo, bolígrafos y lápices usados, heces de animales.";

        infor_2.innerHTML =
          "bolsas de infusión, papel de cocina sucio de aceite y restos de comida, que van al contenedor marrón. Restos de madera, CD, envases que contienen materiales tóxicos y peligrosos, o ropa, que acuden a los Puntos verdes.";

        infor_3.innerHTML =
          "En el contenedor gris acuden todos aquellos residuos que no se pueden recoger de forma selectiva. Todos los residuos se llevan a los ecoparques, donde se separan todos aquellos materiales que se pueden reciclar. Los residuos del contenedor gris que no pueden ser reciclados deben ir a los vertederos o deben ser incinerados. Lo idóneo es que estos tratamientos finalistas sirvan únicamente para los residuos que no se pueden reutilizar o reciclar.";
      }
    },
    error: function (error) {
      console.log("error");
      console.log(error);
    },
  });
}

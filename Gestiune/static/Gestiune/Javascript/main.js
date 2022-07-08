// Functia ce realizeaza animatia din Sistemul de Conectare, footer etc.
(function blink() {
  $('.blink_me').fadeOut(1000).fadeIn(1000, blink);
})();
// Functia ce realizeaza prima animatie, mai exact a cardurilor din prima pagina
$(document).ready(function() {
  new WOW().init();
});
// Functia ce valideaza campurile:
function validateEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

function validateAll() {
  //Aici sunt validarile de la Adaugare/Editare/Vizualizare Pacient
  var numeprenumepacient = $("#numeprenumepacient").val();
  var CNP_Pacient = $("#CNP_Pacient").val();
  var telefon_Pacient = $("#telefon_Pacient").val();
  var emailPacient = $("#emailPacient").val();
  var varsta_Pacient = $("#varsta_Pacient").val();
  var optiune_gen = $("#optiune_gen").val();
  var tip_cetatenie = $("#tip_cetatenie").val();
  var adresa_Pacient = $("#adresa_Pacient").val()
  //Aici sunt validarile de la Adaugare/Editare/Vizualizare FISEI DE PREZENTARE ALE Pacientului
  var simptome_initiale = $("#simptome_initiale").val();
  var optiune_specialitate = $("#optiune_specialitate").val();
  var concluzie_Consult = $("#concluzie_Consult").val();
  var optiune_Decizie = $("#optiune_decizie").val();
  //Aici sunt validarile de la Adaugare/Editare/Vizualizare FISEI DE INTERNARE ALE Pacientului
  var diagnostic_int_initial = $("#diagnostic_int_initial").val();
  var sectie_internare = $("#sectie_internare").val();
  var Epicriza_internare = $("#Epicriza_internare").val();
  var Data_externare_internare = $("#Data_externare_internare").val();




  if (numeprenumepacient == '') {
    swal("Opsss !", "Câmpul NUME nu poate ramane așa..", "error")
    return false;
  }
  //elif pentru a pune si NUME SI PRENUME
  else if (numeprenumepacient.split(' ').length < 2) {
    swal("Opsss !", "Pune și PRENUMELE", "error")
    return false;
  }
  // functie care face din string: ANDREI sau andrei -> 'Andrei' este mai jos; momentan aceasta functie nu permite cuvinte cu UPPER
  else if (numeprenumepacient == numeprenumepacient.toUpperCase()) {
    swal("Opsss !", "Pune și PRENUMELE nu pot fii cu litere MARI!", "error")
    return false;
  } else if (telefon_Pacient == '') {
    swal("Opsss !", "Câmpul TELEFON nu poate ramane așa..", "error")
    return false;
  } else if (CNP_Pacient == '') {
    swal("Opsss !", "Câmpul CNP nu poate ramane așa..", "error")
    return false;
  } else if (emailPacient == '') {
    swal("Opsss !", "Completează cu o adresă de EMAIL validă", "error")
    return false;
  } else if (!(validateEmail(emailPacient))) {
    swal("Opsss !", "Câmpul EMAIL nu poate ramane așa..", "error")
    $("#email").val("");
    return false;
  } else if (varsta_Pacient == '') {
    swal("Opsss !", "Câmpul VÂRSTĂ nu poate ramane așa..", "error")
    return false;
  } else if (optiune_gen == '') {
    swal("Opsss !", "Câmpul GEN nu poate ramane așa..", "error")
    return false;
  } else if (tip_cetatenie == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else if (adresa_Pacient == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  }
  //Aici sunt validarile de la Adaugare/Editare/Vizualizare FISEI DE PREZENTARE ALE Pacientului
  else if (simptome_initiale == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else if (optiune_specialitate == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else if (concluzie_Consult == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else if (optiune_Decizie == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  }
  //Aici sunt validarile de la Adaugare/Editare/Vizualizare FISEI DE INTERNARE ALE Pacientului
  else if (diagnostic_int_initial == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else if (sectie_internare == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else if (Epicriza_internare == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else if (Data_externare_internare == '') {
    swal("Opsss !", "Câmpul Cod Urgenta nu poate ramane așa..", "error")
    return false;
  } else {
    return true;
  }
}
$("#Btn-principal").bind("click", validateAll);
$("#Btn-editeaza").bind("click", validateAll);


function CopiazaCNP() {
  var copyText = document.getElementById("CopiazaCNP");

  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  navigator.clipboard.writeText(copyText.value);

  alert("CNP copiat: " + copyText.value);
}

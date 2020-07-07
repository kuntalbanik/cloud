/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function createCustomer() {

    var custName = $("#custname").val();
    var adDress = $("#address").val();
    var state = $("#state").val();
    var dist = $("#dist").val();
    var city = $("#city").val();
    var postoff = $("#postoff").val();
    var policest = $("#policest").val();
    var pin = $("#pin").val();
    var contactno = $("#contactno").val();
    var contactname = $("#contactname").val();
    var emailid = $("#emailid").val();
    var gstno = $("#gstno").val();

    var enquiryData = JSON.parse(localStorage.getItem("enquiryData"));
    if (enquiryData !== null) {
        enquiryData.companyName = custName;
        enquiryData.aDdress = adDress + ", " + city + ", P.O: " + postoff + ", P.S: " + policest + ", " + pin;
        enquiryData.conTact = contactno;
        enquiryData.dIst = dist;
        enquiryData.statClear = state;
        enquiryData.gSt = gstno;
        enquiryData.contactPer = contactname;

        localStorage.setItem("enquiryData", JSON.stringify(enquiryData));
        window.location.href = "cpupload.php";
    }
}
function returnBack() {
    var enquiryData = JSON.parse(localStorage.getItem("enquiryData"));

    enquiryData.companyName = '';
    enquiryData.aDdress = '';
    enquiryData.conTact = '';
    enquiryData.contactPer = '';

    localStorage.setItem("enquiryData", null);
    window.location.href = "cpupload.php";
}
// Check all required fields 
function formcheck() {
    var a = document.forms["myForm"]["custname"].value;
    var b = document.forms["myForm"]["address"].value;
    var c = document.forms["myForm"]["state"].value;
    var d = document.forms["myForm"]["dist"].value;
    var e = document.forms["myForm"]["state"].value;
    var f = document.forms["myForm"]["city"].value;
    var g = document.forms["myForm"]["postoff"].value;
    var h = document.forms["myForm"]["policest"].value;
    var i = document.forms["myForm"]["pin"].value;
    var j = document.forms["myForm"]["contactno"].value;
    var k = document.forms["myForm"]["contactname"].value;
    // var l=document.forms["myForm"]["emailid"].value;
    var m = document.forms["myForm"]["gstno"].value;

    if (a == "" || b == "" || c == "" || d == "" || e == "" || f == "" || g == "" || h == "" || i == "" || j == "" || k == "" || m == "")
    {
        alert("Please Fill All Required Field");
        return false;
    }
    else {
        if (i.length !== 6 || isNaN(i) || m.length !== 15) {
            alert("Pin code or GST No. incorrect");
            // retrun false;
        }
        else {
            createCustomer();
        }
    }
}

// States
var country_arr = new Array('ASSAM', 'BIHAR', 'CHHATTISGARH', 'DELHI', 'GOA', 'GUJARAT', 'HARYANA', 'JHARKHAND', 'MADHYA_PRADESH', 'MAHARASHTRA', 'MEGHALAYA', 'ODISHA', 'RAJASTHAN', 'UTTAR_PRADESH', 'WEST_BENGAL', 'ANDHRA_PRADESH', 'TRIPURA');
// District
var s_a = new Array();
s_a[0] = "";
s_a[1] = "BARPETA|BONGAIGAON|CACHAR|DARRANG|DHEMAJI|DHUBRI|DIBRUGARH|GOALPARA|GOLAGHAT|HAILAKANDI|JORHAT|KAMRUP|KARBI_ANGLONG|KARIMGANJ|KOKRAJHAR|LAKHIMPUR|MARIGAON|NAGAON|NALBARI|NORTH_CACHAR_HILLS|SIBSAGAR|SONITPUR|TINSUKIA";
s_a[2] = "ARARIA|ARWAL|AURANGABADBH|BANKA|BEGUSARAI|BELAGANJ|BHAGALPUR|BHOJPUR|UXAR|DARBHANGA|EAST_CHAMPARAN|GAYA|GOPALGANJ|JAMUI|JEHANABAD|KAIMUR_BHABUA|KATIHAR|KHAGARIA|KISHANGANJ|LAKHISARAI|MADHEPURA|MADHUBANI|MUNGER|MUZAFFARPUR|NALANDA|NAWADA|PATNA|PURNIA|ROHTAS|SAHARSA|SAMASTIPUR|SARAN|SHEIKHPURA|SHEOHAR|SITAMARHI|SIWAN|SUPAUL|VAISHALI|WEST_CHAMPARAN";
s_a[3] = "BASTAR|BIJAPURCGH|BILASPURCGH|DANTEWADA|DHAMTARI|DURG|GARIABAND|JANJGIR-CHAMPA|JASHPUR|KANKER|KAWARDHA|KORBA|KORIYA|MAHASAMUND|NARAYANPUR|RAIGARH|RAIPUR|RAJNANDGAON|SURGUJA";
s_a[4] = "CENTRAL_DELHI|EAST_DELHI|NEW_DELHI|NORTH_DELHI|NORTH_EAST_DELHI|NORTH_WEST_DELHI|SOUTH_DELHI|SOUTH_WEST_DELHI|WEST_DELHI";
s_a[5] = "NORTH_GOA|SOUTH_GOA";
s_a[6] = "AHMEDABAD|AMRELI|ANAND|BANASKANTHA|BHARUCH|BHAVNAGAR|DAHOD|GANDHI_NAGAR|JAMNAGAR|JUNAGADH|KACHCHH|KHEDA|MAHESANA|NARMADA|NAVSARI|PANCH_MAHALS|PATAN|PORBANDAR|RAJKOT|SABARKANTHA|SURAT|SURENDRA_NAGAR|TAPI|THE_DANGS|VADODARA|VALSAD";
s_a[7] = "AMBALA|BHIWANI|FARIDABAD|FATEHABAD|GURGAON|HISAR|JHAJJAR|JIND|KAITHAL|KARNAL|KURUKSHETRA|MAHENDRAGARH|PANCHKULA|PANIPAT|REWARI|ROHTAK|SIRSA|SONIPAT|YAMUNA_NAGAR";
s_a[8] = "BOKARO|CHATRA|DEOGHAR|DHANBAD|DUMKA|EAST_SINGHBHUM|GARHWA|GIRIDH|GODDA|GUMLA|HAZARIBAG|JAMTARA|KHUNTI|KODERMA|LATEHAR|LOHARDAGA|PAKUR|PALAMAU|RAMGARH|RANCHI|SAHIBGANJ|SERAIKELA-KHARSAWAN|SIMDEGA|WEST_SINGHBHUM";
s_a[9] = "ALIRAJPUR|ANUPPUR|ASHOK_NAGAR|BALAGHAT|BARWANI|BETUL|BHIND|BHOPAL|BURHANPUR|CHHATARPUR|CHHINDWARA|DAMOH|DATIA|DEWAS|DHAR|DINDORI|EAST_NIMAR|GUNA|GWALIOR|HARDA|HOSHANGABAD|INDORE|JABALPUR|JHABUA|KATNI|KHANDWA|KHARGONE|MANDLA|MANDSAUR|MORENA|NARSINGHPUR|NEEMUCH|PANNA|RAISEN|RAJGARH|RATLAM|REWA|SAGAR|SATNA|SEHORE|SEONI|SHAHDOL|SHAJAPUR|SHEOPUR|SHIVPURI|SIDHI|SINGRAULI|TIKAMGARH|UJJAIN|UMARIA|VIDISHA|WEST_NIMAR";
s_a[10] = "AHMED_NAGAR|AKOLA|AMRAVATI|AURANGABAD|BEED|BHANDARA|BULDHANA|CHANDRAPUR|DHULE|GADCHIROLI|GONDIA|INGOLI|JALGAON|JALNA|KOLHAPUR|LATUR|MUMBAI|NAGPUR|NANDED|NANDURBAR|NASHIK|OSMANABAD|PARBHANI|PUNE|RAIGARHMH|RATNAGIRI|SANGLI|SATARA|SINDHUDURG|SOLAPUR|THANE|WARDHA|WASHIM|YAVATMAL";
s_a[11] = "EAST_GARO_HILLS|EAST_KHASI_HILLS|JAINTIA_HILLS|RI_BHOI|SOUTH_GARO_HILLS|WEST_GARO_HILLS|WEST_KHASI_HILLS";
s_a[12] = "ANGUL|BALANGIR|BALASORE|BARGARH|BHADRAK|BOUDH|BHUBANESWAR|CUTTACK|DEBAGARH|DHENKANAL|GAJAPATI|GANJAM|JAGATSINGHAPUR|JAJAPUR|JHARSUGUDA|KALAHANDI|KANDHAMAL|KENDRAPARA|KENDUJHAR|KHORDA|KORAPUT|MALKANGIRI|MAYURBHANJ|NABARANGAPUR|NAYAGARH|NUAPADA|PURI|RAYAGADA|SAMBALPUR|SONAPUR|SUNDERGARH";
s_a[13] = "AJMER|ALWAR|BANSWARA|BARAN|BARMER|BHARATPUR|BHILWARA|BIKANER|BUNDI|CHITTORGARH|CHURU|DAUSA|DHOLPUR|DUNGARPUR|GANGANAGAR|HANUMANGARH|JAIPUR|JAISALMER|JALOR|JHALAWAR|JHUJHUNU|JODHPUR|KARAULI|KOTA|NAGAUR|PALI|RAJSAMAND|SAWAI_MADHOPUR|SIKAR|SIROHI|TONK|UDAIPUR";
s_a[14] = "AGRA|ALIGARH|ALLAHABAD|AMBEDKAR_NAGAR|AURAIYA|AZAMGARH|BAGPAT|BAHRAICH|BALLIA|BALRAMPUR|BANDA|BARABANKI|BAREILLY|BASTI|BIJNOR|BUDAUN|BULANDSHAHR|CHANDAULI|CHITRAKOOT|DEORIA|ETAH|ETAWAH|FAIZABAD|FARRUKHABAD|FATEHPUR|FIROZABAD|GAUTAM_BUDDHA_NAGAR|GHAZIABAD|GHAZIPUR|GONDA|GORAKHPUR|HAMIRPUR|HARDOI|HATHRAS|JALAUN|JAUNPUR|JHANSI|JYOTIBA_PHULE_NAGAR|KANNAUJ|KANPUR_DEHAT|KANPUR_NAGAR|KAUSHAMBI|KHERI|KUSHINAGAR|LALITPUR|LUCKNOW|MAHARAJGANJ|MAHOBA|MAINPURI|MATHURA|MAU|MEERUT|MIRZAPUR|MORADABAD|MUZAFFARNAGAR|NAUTANWA|PILIBHIT|PRATAPGARH|RAEBARELI|RAMPUR|SAHARANPUR|SANT_KABIR_NAGAR|SANT_RAVIDAS_NAGAR|SHAHJAHANPUR|SHRAWASTI|SIDDHARTHNAGAR|SITAPUR|SONBHADRA|SULTANPUR|UNNAO|VARANASI";
s_a[15] = "BANKURA|BARDHAMAN|BIRBHUM|COOCH_BEHAR|DARJILING|EAST_MIDNAPORE|HOOGHLY|HOWRAH|JALPAIGURI|KOLKATA|MALDA|MEDINIPUR|MURSHIDABAD|NADIA|NORTH_24_PARGANAS|NORTH_DINAJPUR|PURULIYA|SOUTH_24_PARGANAS|SOUTH_DINAJPUR|WEST_MIDNAPORE";
s_a[16] = "Anantapur|Chittoor|East Godavari|Kadapa|Krishna|Kurnool|Nellore|Prakasam|Srikakulam|Visakhapatnam|Vizianagaram|West Godavari";
s_a[17] = "Dhalai|Sipahijala|Khowai|Gomati|Unakoti|North_Tripura|South_Tripura|West_Tripura";                                       // State and District function select to change

function populateStates(countryElementId, stateElementId) {
    var selectedCountryIndex = document.getElementById(countryElementId).selectedIndex;
    var stateElement = document.getElementById(stateElementId);
    stateElement.length = 0; // Fixed by Julian Woods
    stateElement.options[0] = new Option('', '');
    stateElement.selectedIndex = 0;
    var state_arr = s_a[selectedCountryIndex].split("|");
    for (var i = 0; i < state_arr.length; i++) {
        stateElement.options[stateElement.length] = new Option(state_arr[i], state_arr[i]);
    }
}

function populateCountries(countryElementId, stateElementId) {
    // given the id of the <select> tag as function argument, it inserts <option> tags
    var countryElement = document.getElementById(countryElementId);
    countryElement.length = 0;
    countryElement.options[0] = new Option('', '');
    countryElement.selectedIndex = 0;
    for (var i = 0; i < country_arr.length; i++) {
        countryElement.options[countryElement.length] = new Option(country_arr[i], country_arr[i]);
    }
    // Assigned all countries. Now assign event listener for the states.
    if (stateElementId) {
        countryElement.onchange = function() {
            populateStates(countryElementId, stateElementId);
        };
    }
}
populateCountries("state", "dist");
populateCountries("state2", "dist2");





function copyData() {
    document.getElementById("address2").value = document.getElementById("address").value;
    document.getElementById("state2").value = document.getElementById("state").value;
    populateStates("state2", "dist2");
    document.getElementById("dist2").value = document.getElementById("dist").value;
    //document.getElementById("state2").style.borderColor = "red";
    //document.getElementById("dist2").style.borderColor = "red";
    document.getElementById("pin2").value = document.getElementById("pin").value;
    document.getElementById("contactno2").value = document.getElementById("contactno").value;
    document.getElementById("emailid2").value = document.getElementById("emailid").value;
    document.getElementById("gstno2").value = document.getElementById("gstno").value;
    document.getElementById("cinno2").value = document.getElementById("cinno").value;
    
    
}



//var fields = [id_search, address, state, dist, pin, contactno, emailid, gstno, cinno, address2, state2, dist2, pin2, contactno2, emailid2, gstno2, cinno2];
//                                id_search = document.forms["insertaddr"]["id_search"].value;
//                                address = document.forms["insertaddr"]["address"].value;
//                                state = document.forms["insertaddr"]["state"].value;
//                                dist = document.forms["insertaddr"]["dist"].value;
//                                pin = document.forms["insertaddr"]["pin"].value;
//                                contactno = document.forms["insertaddr"]["contactno"].value;
//                                emailid = document.forms["insertaddr"]["emailid"].value;
//                                gstno = document.forms["insertaddr"]["gstno"].value;
//                                cinno = document.forms["insertaddr"]["cinno"].value;
//                                address2 = document.forms["insertaddr"]["address2"].value;
//                                state2 = document.forms["insertaddr"]["state2"].value;
//                                dist2 = document.forms["insertaddr"]["dist2"].value;
//                                pin2 = document.forms["insertaddr"]["pin2"].value;
//                                contactno2 = document.forms["insertaddr"]["contactno2"].value;
//                                emailid2 = document.forms["insertaddr"]["emailid2"].value;
//                                gstno2 = document.forms["insertaddr"]["gstno2"].value;
//                                cinno2 = document.forms["insertaddr"]["cinno2"].value;
                                
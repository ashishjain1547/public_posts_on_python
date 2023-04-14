let jsonstreng_with_key = {
    "kjennemerke": 1
} 

let jsonstreng_without_key = {} // Empty object 

if(jsonstreng_with_key.hasOwnProperty('kjennemerke')){
    console.log("jsonstreng_with_key has key 'kjennemerke'");
} else {
    console.log("jsonstreng_with_key does not have key 'kjennemerke'");
}

if(jsonstreng_without_key.hasOwnProperty("kjennemerke")){
    console.log("jsonstreng_without_key has key 'kjennemerke'");
} else {
    console.log("jsonstreng_without_key does not have key 'kjennemerke'");
}


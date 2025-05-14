$("#add").click(addContact);
$("#retrieve").click(retrieveContactButton);
$("#print").click(printContacts);

var phonebook = [];

if(localStorage.getItem("phonebook")) {
    
    phonebook = JSON.parse(localStorage.getItem("phonebook"));
    
}

function addContact() {
    
    var firstName = prompt("Enter contact's first name: ");
    var lastName = prompt("Enter contact's last name: ");
    var phoneNumber = prompt("Enter contact's phone number: ")
    
    if(firstName == null || lastName == null || phoneNumber == null ||
        firstName == "" || lastName == "" || phoneNumber == "")
    {
        throw new Error("name or number is null");
    }

    phonebook.push({
        
        firstName: firstName,
        lastName: lastName,
        phoneNumber: phoneNumber,
        
    });
    
    localStorage.setItem("phonebook", JSON.stringify(phonebook));
    
}

function retrieveContactButton() {
    
    var firstName = prompt("Enter contact's first name: ");
    var lastName = prompt("Enter contact's last name: ");
    
    if(contactExists(firstName, lastName)) {
        
        retrieveContact(firstName, lastName);
        
    } else {
        
        var contactToAdd = prompt("Contact not found, add to your contacts (Y/n)? ");
        
        if(contactToAdd == "Y" || contactToAdd =="y") {
            
            addContact();
            
        }
        
    }
    
}

function contactExists(first, last) {
    
    for(var i = 0; i < phonebook.length; i++) {
        console.log("loop: " + i);
        if(phonebook[i].firstName == first && phonebook[i].lastName == last) {
            
            console.log("true");

            return true;
            
        }
        
    }

    return false;
    
}
    
function retrieveContact(first, last) {
    
    var list = document.createElement("ul");
    
    var listElement = document.createElement("li");
    
    for(var i = 0; i < phonebook.length; i++) {
        
        if(phonebook[i].firstName == first && phonebook[i].lastName == last) {
            
            listElement.innerHTML = phonebook[i].firstName + " " + phonebook[i].lastName + " " + phonebook[i].phoneNumber;
            
        }
        
    }
    
    list.append(listElement);
    
    $("#contact-reveal").append(list);
    
}

function printContacts() {
    
    $("#contact-reveal").html("");
    
    var list = document.createElement("ul");
    
    for(var i = 0; i < phonebook.length; i++) {
        
        var listElement = document.createElement("li");
        
        listElement.innerHTML = phonebook[i].firstName + " " + phonebook[i].lastName + " " + phonebook[i].phoneNumber;
        
        list.append(listElement);
        
    }
    
    $("#contact-reveal").append(list);
    
}

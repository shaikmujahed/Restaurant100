function validate()
{
    if(document.myform.Username.value=="")
    {
        alert("please provide your user name");
        document.myform.Username.focus();
        return false;
    }
    if(document.myform.number.value=="")
    {
        alert("please provide your phone number");
        document.myform.number.focus();
        return false;
    }
    if(document.myform.mail.value=="")
    {
        alert("please provide your mailid");
        document.myform.mail.focus();
        return false;
    }
    if(document.myform.Password.value=="")
    {
        alert("please provide your password");
        document.myform.Password.focus();
        return false;
    }
    if(document.myform.Password1.value=="")
    {
        alert("please provide your password");
        document.myform.Password1.focus();
        return false;
    }
}
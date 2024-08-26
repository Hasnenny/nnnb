if($text == "قران" or $text == "ق"){
bot("sendvoice",[
"chat_id"=>$chat_id,
"voice"=>"https://t.me/QuranYatChannel/" . rand(4,226),
"caption"=>"» م تصلي علي النبي 🙂"
]);
}

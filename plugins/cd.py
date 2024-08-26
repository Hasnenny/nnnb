$chi = botatiiii; 
if($text == "كت ص" or $text == "كتص"){
bot("sendphoto",[
"chat_id"=>$chat_id,
'reply_to_message_id'=>$message->message_id, 
"photo"=>"https://t.me/cuthms/" . rand(2,49),
"caption"=>"» كت تويت بالصورة ♡ 🙂
@Kttoeetbot",
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>'true',
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"- $name .",'url'=>"t.me/$chi"]],
]])]);}
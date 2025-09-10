
 To run the project, you need to run the BAT file on the terminal on your computer. Note that the PATH for podcasts on your computer is the same as the PATH.
 In addition, you can set the rest of the ENVIROMENT to your own or the program will use the default path.



In terms of scheduling the system that will transcribe the audio file, 
there are two options with different considerations:
1 - either the system will upload the JSON with the transcription already in it to ELASTICSEARCH,
or the system will upload only the JSON with the METADATA to ELASTIC and there will be a separate process that runs separately upon request or on a fixed schedule that goes through the entire ELASTIC,
2 - checks if the transcribed file is already there, and if not, then it updates it and adds it.

The advantage of the first approach is that no matter when I pull out ELASTIC, the transcribed file will always be there.
Your problem is that it has significant drawbacks - the system that saves the information becomes very slow because it does not upload a document to ELASTIC until it transcribes it
And in an operational situation, I think it is better that first all the DATA is saved well and only then start processing it
So that if they need to retrieve the most important information, first of all it will exist in a certain way, even if not ideal,
And so I chose to use the second approach, where the system operates separately and when necessary and able or at a fixed time it goes through all the information in MONGO and checks in ELASTIC if it has already
been transcribed and transcribes when necessary, that way the information is always saved first, the system does not become slow and in an emergency I always have the basic information at least and 
probably also the transcribed one if the system was operated with the right discretion.
In fact, in terms of code, I have both approaches, and if in terms of computing capabilities,
if there is only one really powerful computer, maybe it would be better to have two systems than a weak processor, 
so if you want to choose the first approach, you need to activate the lines of code between lines 18 - 22 in the MAIN file in the "DataPersister" folder and simply not activate the separate system.



I calculate the risk level of a text based on the ratio between the number of risk points and the number of words.
Low-risk words are worth one point, and high-risk words are worth two.
This gives me a measure that shows how "saturated" the text is with problematic words – not just how many occurrences there are, 
but also what their weight is in the entire content.

I set a threshold score — a number that marks the point where the text becomes concerning.

The score is based on the ratio between the number of risky words and the total number of words in the text.

I chose a threshold of 0.025, meaning that if 0.025  or more of the words in the text are risky, the text will be flagged.
This value was chosen because it gives a good balance:
It catches texts that are clearly problematic, but avoids flagging texts that are mostly neutral or harmless.



I use three risk levels based on the number of dangerous words in the text:
less than  0.0125 = safe - bed word from  80 word ()
over 0.05 = high risk  - bed word from  20 word ()
0.0125  to  0.05 = medium risk
These numbers were chosen because they provide a clear separation between harmless, somewhat dangerous, and very dangerous texts - based on tests I conducted on real examples


Regarding the choice of ENDPOINT
I chose to retrieve all DOC with RISKLEVEL according to a user request, which I think is most useful to retrieve all those with high risk or rather the medium one
Another ENDPOINT I made is to receive all DOCs with a risk percentage higher or lower than a number - the user will enter whether they want it higher or lower and also the number/percentage they want.
This additional ENDPOINT will be added to the DOC club based on the ID received from the user.
Another very effective and thoughtful ENDPOINT is deleting the entire DOC with LEVELRISK that will be given by the user, for example,
if it was decided that it is not relevant to those who have RISKLEVEL NONE and it is a shame about the large amount of space that this DATA will take up,
then this way you can delete it and use the space that will be freed up.
PING - check the connection to ELASTIC


Default MAPPING:

index_mapping = {
"mappings": {
"properties": {
"Name": {"type": "keyword"},
"Stem": {"type": "keyword"},
"Suffix": {"type": "keyword"},
"Parent": {"type": "keyword"},
"File size": {"type": "integer"},
"Last modified": {"type": "keyword"},
"creation_datetime": {"type": "keyword"} ,
"file path with type": {"type": "keyword"} ,
"file path": {"type": "keyword"} ,
"transcription_audio" : {"type": "keyword"} ,
"is_bds" : {"type": "boolean"} ,
"bds_threat_level" : {"type": "keyword"}  ,
"bds_percent" :{"type":  "double"}

}
}
}
##################################################
Possible environment variables to set:

PATH_TO_DIRECTORY 
UNIQUE_FIELD_INDENTIFIER_IN_JSON 
PATH_KEY_IN_DOC  
NAME_KEY_IN_DOC 
SIZE_NAME_IN_DOC 
TOPIC_FOR_KAFKA 
INDEX_NAME 
INDEX_MAPPING
DB_NAME 

URI 
COLLECTION_NAME 
SCHEMA_elastic 
# HOST_ELASTIC
HOST_ELASTIC 
PORT_ELASTIC
LOGGER_PODCAST_INDEX_NAME 
LOGGER_PODCAST_NAME 
NAME_TEMPORARY_WAV_PATH_FILE
NAME_FIELD_TRANSCRIPTION_AUDIO
THRESHOLD_DANGEROUS_WORD 
LIST_WORD_VERY_HOSTILE_STRING_BASE64 
LIST_WORD_LESS_HOSTILE_STRING_BASE64 

VERY_DANGEROUS_WORS_SCORE 
LESS_DANGEROUS_WORS_SCORE 

NAME_FAILD_FOR_IS_BDS
NAME_FAILD_FOR_BDS_THREAT_LEVEL
NAME_FAILD_FOR_BDS_PERCENT 
REBOOT_TIME_TRANSCRIPTION  
REBOOT_TIME_CALCULATION_PERCENTAGE_OF_DANGER 

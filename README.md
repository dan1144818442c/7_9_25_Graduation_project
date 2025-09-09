
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

if (args.Length < 1)
{
    Console.WriteLine("no args found; run it properly via \"dotnet run -- <path-to-csv>\"");
}

int longitudeColumn = -1;
int latitudeColumn = -1;

float maxLongitude = float.MinValue;
float minLongitude = float.MaxValue;
float maxLatitude = float.MinValue;
float minLatitude = float.MaxValue;

int linesRead = 0;
List<string> currentTokens;
using (StreamReader streamReader = new(args[0]))
{
    while (!streamReader.EndOfStream)
    {
        currentTokens = Tokenizer.TokenizeRow(streamReader.ReadLine());
        linesRead++;
        if (linesRead == 1)
        {
            for (int i = 0; i < currentTokens.Count(); i++)
            {
                string lowercaseToken = currentTokens[i].ToLower();
                if (lowercaseToken.Contains("longitude"))
                {
                    longitudeColumn = i;
                }
                else if (lowercaseToken.Contains("latitude"))
                {
                    latitudeColumn = i;
                }

                if (longitudeColumn >= 0 && latitudeColumn >= 0)
                {
                    break;
                }
            }

            if (latitudeColumn < 0 || longitudeColumn < 0)
            {
                string warning = "could not find the following columns:\n";
                if (latitudeColumn < 0)
                    warning += "Latitude\n";
                if (longitudeColumn < 0)
                    warning += "Longitude\n";

                Console.WriteLine(warning);
                break;
            }

            continue;
        }

        if (!float.TryParse(currentTokens[longitudeColumn], out var longitude))
        {
            Console.WriteLine($"failed to parse longitude from {currentTokens[longitudeColumn]}");
        }
        if (!float.TryParse(currentTokens[latitudeColumn], out var latitude))
        {
            Console.WriteLine($"failed to parse longitude from {currentTokens[latitudeColumn]}");
        }

        maxLongitude = float.Max(longitude, maxLongitude);
        minLongitude = float.Min(longitude, minLongitude);
        maxLatitude = float.Max(latitude, maxLatitude);
        minLatitude = float.Min(latitude, minLatitude);
    }
}

if (maxLongitude == float.MinValue)
{
    Console.WriteLine("Failed to find a max longitude");
}
if (minLongitude == float.MaxValue)
{
    Console.WriteLine("Failed to find a min longitude");
}

if (maxLatitude == float.MinValue)
{
    Console.WriteLine("Failed to find a max latitude");
}
if (minLatitude == float.MaxValue)
{
    Console.WriteLine("Failed to find a min latitude");
}

Console.WriteLine($"lon: {minLongitude}, {maxLongitude}");
Console.WriteLine($"lat: {minLatitude}, {maxLatitude}");

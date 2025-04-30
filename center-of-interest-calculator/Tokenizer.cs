public static class Tokenizer
{
    public static List<string> TokenizeRow(string row)
    {
        List<string> tokens = new();

        if (string.IsNullOrWhiteSpace(row))
        {
            return tokens;
        }

        int fieldStartIndex = 0;
        bool inQuotes = false;
        for (int i = 0; i < row.Length; i++)
        {
            char currentChar = row[i];
            if (currentChar == ',' && !inQuotes)
            {
                tokens.Add(row.Substring(fieldStartIndex, i - fieldStartIndex));
                fieldStartIndex = i + 1;
                continue;
            }
            if (currentChar == '"')
            {
                inQuotes = !inQuotes;
            }
        }
        tokens.Add(row.Substring(fieldStartIndex));

        return tokens;
    }
}

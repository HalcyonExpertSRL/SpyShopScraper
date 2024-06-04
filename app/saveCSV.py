import saveProducts
import pandas as pd
import json
class CSV():
    def checkAttr(self, URL):
        try:
            requestInstance = saveProducts.getProduct()
            lista = requestInstance.getProductAttr(URL)
            for item in lista:
                for item2 in item:
                    print(f"{item2}XD")
                    with open('test.csv', 'a') as file:
                        if 'id' in item2 or 'name' in item2 or 'price' in item2:
                            item2 = item2.replace(", ", " ")
                            item2 = item2.replace("                ", "")
                            file.write(f"{item2}\n")
            return "Done"
        except Exception as e:
            return f"Error occurred: {str(e)}"

    def mergeLines(self):
        try:
            with open('test.csv', 'r') as file:
                lines = file.readlines()
            merged_lines = [','.join(lines[i:i+4]).replace('\n', '') for i in range(0, len(lines), 4)]
            with open('merged.csv', 'w') as file:
                file.write('\n'.join(merged_lines))
            return "Merged lines and saved to merged.csv"
        except Exception as e:
            return f"Error occurred: {str(e)}"

    def saveToJson(self):
                    try:
                        data = []
                        with open('test.csv', 'r') as file:
                            lines = file.readlines()
                        for line in lines:
                            values = line.strip().split(',')
                            if len(values) == 3:
                                item = {
                                    'id': values[0],
                                    'name': values[1],
                                    'price': values[2]
                                }
                                data.append(item)
                        with open('result.json', 'w') as file:
                            json.dump(data, file)
                        return "Saved result to result.json"
                    except Exception as e:
                        return f"Error occurred: {str(e)}"
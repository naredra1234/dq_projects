from read import load_data

data = load_data()
data["subdomain"] = data["url"].apply(lambda x: "".join(str(x).split(".")[1:]))
domains = data["url"].value_counts()
subdomains = data["subdomain"].value_counts()
print (domains[0:4])
print (subdomains[0:4])

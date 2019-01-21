If you did del some_object

follow it up with torch.cuda.empty_cache()

This will allow the reusable memory to be freed (You may have read that pytorch reuses memory after a del some _object)

This way you can see what memory is truly avalable


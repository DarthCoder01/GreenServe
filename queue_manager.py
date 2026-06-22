job_queue = []

job_counter = 0

def add_job(priority):

    global job_counter

    job_counter += 1

    job = {
        "id": job_counter,
        "priority": priority
    }

    job_queue.append(job)

    return job

def get_queue():
    return job_queue

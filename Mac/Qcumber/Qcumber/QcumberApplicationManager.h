//
//  QcumberApplicationManager.h
//  Qcumber
//
//  Created by Chris Cooper on 11-10-13.
//  Copyright 2011 Chris Cooper. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface QcumberApplicationManager : NSObject {
    NSPersistentStoreCoordinator *__persistentStoreCoordinator;
    NSManagedObjectModel *__managedObjectModel;
    NSManagedObjectContext *__managedObjectContext;
}

@property (readonly, strong, nonatomic) NSPersistentStoreCoordinator *persistentStoreCoordinator;
@property (readonly, strong, nonatomic) NSManagedObjectModel *managedObjectModel;
@property (readonly, strong, nonatomic) NSManagedObjectContext *managedObjectContext;

@end
